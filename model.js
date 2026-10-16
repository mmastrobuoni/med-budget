(function(root){
'use strict';
const sum=a=>a.reduce((s,v)=>s+v,0), finite=(n,min,max)=>Number.isFinite(Number(n))?Math.max(min,Math.min(max,Number(n))):min;
function defaults(data){
 const rates={};
 for(const key of ['wages','operating','insurance','pension','schools','assessments','debt']){
  const accounts=data.departments.filter(d=>d.included&&!d.note.includes('not comparable')&&!d.note.includes('crosswalk')).flatMap(d=>d.accounts).filter(a=>a.driver===key&&a.values.slice(0,4).every(v=>v!==null&&v>0));
  const totals=[0,1,2,3].map(i=>sum(accounts.map(a=>a.values[i])));
  const changes=[1,2,3].filter(i=>totals[i-1]>0).map(i=>100*(totals[i]/totals[i-1]-1)).sort((a,b)=>a-b);
  rates[key]=key==='debt'?0:Math.round(Math.max(0,Math.min(15,changes[1]??3))*10)/10;
 }
 return {version:data.version,rates,revenueRates:{'Property Taxes':2.5,'State Aid':2,'Local Receipts':2,'Federal Aid':0,'Transfers In':0},newGrowth:2100000,recurringRevenue:0,revenueStart:2028,reservePool:0,reserveAnnual:0,adjustments:{},accountRates:{},investments:[]};
}
function sanitize(raw,data){
 const s=defaults(data);if(!raw||typeof raw!=='object'||raw.version!==data.version)return s;
 for(const k in s.rates)if(raw.rates?.[k]!==undefined)s.rates[k]=finite(raw.rates[k],-20,30);
 for(const k in s.revenueRates)if(raw.revenueRates?.[k]!==undefined)s.revenueRates[k]=finite(raw.revenueRates[k],-20,20);
 for(const k of ['newGrowth','recurringRevenue','reservePool','reserveAnnual'])s[k]=finite(raw[k]??0,0,1e9);
 s.revenueStart=Math.round(finite(raw.revenueStart??2028,2028,2032));
 for(const d of data.departments){if(!d.included)continue;if(raw.adjustments?.[d.id]!==undefined)s.adjustments[d.id]=finite(raw.adjustments[d.id],-100,100);for(const a of d.accounts)if(raw.accountRates?.[a.id]!==undefined)s.accountRates[a.id]=finite(raw.accountRates[a.id],-20,30);}
 if(Array.isArray(raw.investments))s.investments=raw.investments.slice(0,30).filter(x=>x&&typeof x==='object').map((x,i)=>({id:'investment-'+i,name:String(x.name||'Investment').slice(0,100),amount:finite(x.amount,0,1e9),start:Math.round(finite(x.start,2028,2032)),kind:x.kind==='once'?'once':'recurring',growth:finite(x.growth??3,-20,30)}));
 return s;
}
function project(data,state){
 const s=sanitize(state,data), baseR=data.summary.budgetRevenue[5],baseE=data.publishedTotal;
 let taxes=data.revenues['Property Taxes'][5],reserve=s.reservePool;
 const out=[];
 for(let n=0;n<=5;n++){
  const year=2027+n;
  if(n>0)taxes=taxes*(1+s.revenueRates['Property Taxes']/100)+s.newGrowth;
  const extra=year>=s.revenueStart?s.recurringRevenue*Math.pow(1.025,year-s.revenueStart):0;
  const revenue=taxes+sum(Object.keys(s.revenueRates).filter(k=>k!=='Property Taxes').map(k=>data.revenues[k][5]*Math.pow(1+s.revenueRates[k]/100,n)))+extra;
  const depts=data.departments.filter(d=>d.included).map(d=>({id:d.id,name:d.name,amount:sum(d.accounts.filter(a=>a.values[5]!==null).map(a=>a.values[5]*Math.pow(1+(s.accountRates[a.id]??s.rates[a.driver])/100,n)))*(n?1+(s.adjustments[d.id]??0)/100:1)}));
  const investments=s.investments.filter(x=>year>=x.start&&(x.kind==='recurring'||year===x.start));
  const recurringInvestment=sum(investments.filter(x=>x.kind==='recurring').map(x=>x.amount*Math.pow(1+x.growth/100,year-x.start)));
  const oneTime=sum(investments.filter(x=>x.kind==='once').map(x=>x.amount));
  const recurringExpense=sum(depts.map(d=>d.amount))+data.reconciliationDifference+recurringInvestment;
  const expense=recurringExpense+oneTime;
  // Compare changes to the published base; unresolved original funding is disclosed separately.
  const structuralGap=(recurringExpense-baseE)-(revenue-baseR);
  const incrementalGap=(expense-baseE)-(revenue-baseR);
  const draw=n?Math.min(reserve,s.reserveAnnual,Math.max(0,incrementalGap)):0;reserve-=draw;
  out.push({year,revenue,expense,structuralGap,incrementalGap,draw,reserve,remainingGap:incrementalGap-draw,fullDifference:expense-revenue-draw,depts,recurringInvestment,oneTime});
 }
 return out;
}
const api={defaults,sanitize,project};root.BudgetModel=api;if(typeof module!=='undefined')module.exports=api;
})(typeof window==='undefined'?globalThis:window);
