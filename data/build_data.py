"""Reproducible transcription of public chart labels retrieved 2026-10-16.
Columns: FY22–25 actual; FY26 and FY27 published budget. Never infer missing zero.
Account labels are source categories, not verified numeric prime-account codes.
"""
import json,csv
from pathlib import Path
P=Path(__file__).parent
rows=[]
def add(name,slug,group,accounts,note=''):
 rows.append(dict(id=slug,name=name,group=group,url='https://city-medford-ma-budget-book.cleargov.com/21444/departments/'+slug,accounts=[dict(name=k,values=v) for k,v in accounts.items()],note=note))
O='Ordinary Expenses'; W='Personnel Expenses'; T='Department total — account detail unavailable'
add('Executive Office','executive-office','General government',{O:[112162.74,107462.57,111829.96,107119.49,118150,124068.99],W:[789767.01,478839.4,521479.94,546473.13,572238,610560.33]},'FY22 and FY23 include contractual agreements not represented in later years; historical growth is not comparable without adjustment.')
add('Legislative','legislative','General government',{O:[34338.9,32197.68,84568.13,64209.31,80100,50100],W:[212354.28,215687.96,219664.84,217029.78,227259,232774]})
add('Law','law','General government',{W:[198924.53,121831.97,76899.79,105399.43,236828,230866.6],O:[342002.87,231912.02,298296.52,443806.16,288400,298700]},'Published book amount; reconcile Council reductions before calling this adopted.')
add('City Clerk','city-clerk','General government',{O:[17394.34,12434.48,9282.7,15983.61,21150,16950],W:[328462.87,312276.27,359262.52,315346,387536,347606.72]})
add('Elections','elections','General government',{O:[48456.68,82166.69,89129.47,36261.81,116580,68100],'Elections':[None,None,None,111909.32,88000,134000],W:[329823.99,240991,284361.71,213697.82,190349,283231.63]})
add('Diversity, Equity & Inclusion','diversity-equity-inclusion','General government',{O:[3872.47,1246.09,2963.15,12608.19,18400,18900],W:[184577.49,97469.54,104574.17,99468.06,111511,130461.76]})
add('Human Resources','human-resources','General government',{O:[7592.17,6547.68,7863.09,8180.87,46500,57122.5],W:[54061.13,179791.52,208013.52,253501.49,273993,306061.21]})
add('Information Technology','information-technology','General government',{W:[142139.56,61982,117925.77,119602.9,122137,125191.04],O:[208419.05,192000.54,274095.57,157703.6,238120,396120]})
add('Finance / Procurement','finance-procurement','General government',{O:[113327.76,137263.77,155231.14,292062.8,259840,262740],W:[464174.06,539258.23,594412.12,594205.32,620295,635078.45]})
add('Treasurer / Collector','treasurer-collector','General government',{'Personnel':[None,None,None,19731.3,26006,26403.04],O:[232303.56,269442.13,283869.62,288420.73,282225,300675],W:[403534.33,446048.13,397041.14,442293.18,471828,487128.25]})
add('Assessor','assessor','General government',{O:[131670.47,127678.29,159744.23,168752.62,225175,164280],W:[316975.68,328433.59,397374.99,369748.47,419637,428049.09]})
add('Planning, Development & Sustainability','planning-development-sustainability','Community development',{'Personnel Expenses — source series 1':[69565.77,73764.6,84761.89,None,None,None],'Ordinary Expenses — source series 1':[142478.07,102240.18,210308.17,995,None,None],O:[11798.46,13684.41,23090.44,149151.43,227120,150100],W:[270667.68,285007.8,455390.42,629630.06,696043,722105.83]},'Multiple source series share account labels; retained separately. Historical organizational crosswalk pending.')
add('Medford Community Media','peg-access-medford-community-media','Separate fund',{'Cable':[None,None,None,2160,2000,2000],O:[60476.14,84167.28,37892.72,40520.63,49000,49000],W:[93294.44,127489.62,128632.21,137341.89,164061,225101.97]},'FY27 PEG special revenue fund; excluded from General Fund scenario. Earlier-year fund scope requires crosswalk.')
add('Chevalier Theatre','chevalier-theatre','Culture & recreation',{T:[31630.5,30765.75,31369,30890.02,None,None]},'Consolidated into Facilities in current book. Missing current value is not assumed to be zero.')
add('Police','police-department','Public safety',{O:[685805.01,638313.79,755913.82,736126.99,831356,771145],W:[13327045.92,12725085,13187719.05,13522027.94,14252541,16711653.91]})
add('Traffic Supervisors','traffic-supervisors','Public safety',{O:[3415.86,3367.79,7371,6316.96,9000,9000],W:[298223.6,302858.3,316969.27,324634.35,361500,371025]})
add('Fire','fire-department','Public safety',{O:[488497.3,567850.14,530494.7,554786.34,610250,726500],W:[13203446.94,13366682.62,14073596.46,14801180.97,15192244,15282563.78]})
add('Building','building-department','Public safety',{T:[921455.88,1044711.94,1012093.39,1051578.07,1057806,1110890.48]},'Source account charts are empty; retain department total without inventing a salary/operating split.')
add('Parking','parking','Public safety',{O:[171970.33,402992.51,317159.42,425132,292307,299370.11],W:[257819.01,597982.02,652594.77,684562.42,770433,789819.33]})
add('Electrical','electrical','Public safety',{W:[352037.55,336989.97,326122.07,306018.12,322869,345542.72],O:[301532.77,425817.83,357650.45,369719.82,429225,444725]})
add('Public Works','department-of-public-works-dpw','Public works',{'Forestry':[390206.21,444309.88,545613.5,497943.37,618365,613088.96],'Engineering':[465113.09,464236.81,518905.32,450631.98,719082,736479.03],'Parks':[798719.77,739797.96,824028.22,798988.24,954765,937625.81],'Cemetery':[915474.43,965617.36,1070438.07,1034865.17,1072842,1086657.97],'Highway':[11021959.41,10806051.06,11104900.93,11669536.42,14029809,15011756.92]},'Source shows divisions rather than prime accounts. Division growth controls are available; personnel split pending.')
add('Water / Sewer','dpw-water-sewer-enterprise','Separate fund',{W:[1479493.07,1629196.12,1639610.25,1540103.01,2093885,2111870.47],'Other Financing':[1607264,1770000,1600000,4182617.96,2163030.32,2163030.32],O:[21494781.95,22388779.71,23271786.78,23910296.87,24847137,25588171.71]},'Enterprise fund; excluded from General Fund scenario. Debt also appears in a separate debt department.')
add('Facilities','facilities','Public works',{T:[1102096.81,1315540.58,1800442.03,1691878.33,2102129,2212294.55]})
add('Health & Human Services','board-of-health','Health & human services',{'Ordinary Expenses — source series 1':[28406.85,36912.02,39639.63,23518.86,32850,56300],O:[31588.52,32622.91,37608.45,47163.56,55350,102137],W:[666606.07,621964.74,551040.38,723535.66,867379,883980.46]})
add('Emergency Management','civil-defense','Public safety',{O:[None,None,299.67,None,1000,400],W:[9089.92,7506.6,8839.92,8839.92,8840,8840]})
add('Council on Aging','council-on-aging','Health & human services',{O:[14810.61,16327.64,17433.41,14422.6,16000,16582],W:[222017.66,220681.95,241082.75,262631.18,190057,190486.03]})
add('Library','library','Culture & recreation',{O:[305379.06,306406.05,470337.94,541670.45,591500,598500],W:[1230020.7,1421440.6,1542460.96,1650057.75,1640439,1822565.52]})
add('Recreation','recreation','Culture & recreation',{T:[482502.39,577074.94,586723.34,658279.84,639351,682126.96]})
add('Veterans Services','veterans-services','Health & human services',{'Ordinary Expenses — source series 1':[12603,7483.36,7670.91,13520.33,15000,15000],W:[103224.18,108704.37,99264.25,119151.34,129002,142527.28],O:[250974.34,201639.52,179461.08,161554.75,304714,284132]})
add('Bicycle Commission','bicycle-commission','Culture & recreation',{T:[835,1392.01,1500,0,1500,2200]})
add('Community Development Board','community-development-board','Community development',{O:[149,167.14,None,None,300,300],W:[7418.75,6431.22,6900,7000,9800,14300]})
add('Conservation Commission','conservation-commission','General government',{O:[837.92,597,609,621,1100,1100],W:[5200,5200,4600,5800,6400,5750]})
add('Historic District Commission','historic-district-commission','General government',{T:[4259.5,4525,0,1232,5000,5000]})
add('Historical Commission','historical-commission','Culture & recreation',{T:[17464.98,20495.69,20338.32,25748.85,35000,35000]})
add('Hormel Commission','hormel-commission','Culture & recreation',{T:[5699.94,5399.94,4499.94,4703.78,5400,5400]})
add('License Commission','license-commission','General government',{O:[None,None,None,None,400,400],W:[3750,3067.31,4500,4500,5400,4500]})
add('Traffic Commission','traffic-commission','Public safety',{W:[5050.68,4500,4500,4500,4500,4500],O:[21544,22956.77,22300,22500,26000,26000]})
add('Zoning Board of Appeals','zoning-board-of-appeals','General government',{T:[8500,11000,9750,11500,12500,12500]})
add('Workers Compensation','workers-compensation','Benefits & insurance',{O:[76788.76,85106.03,68791.89,21233.17,30000,30000],W:[806742.84,762067.38,907981.45,1154245.47,898000,1183000]})
add('Insurance','insurance','Benefits & insurance',{O:[531720.36,612874.04,696857.04,748827.04,775000,809875],W:[23462406.13,24553750.31,25872846.9,27506881.04,30445000,33273325]},'Personnel Expenses here represent insurance costs, not ordinary wages. Use insurance growth driver.')
add('Pensions','pensions','Benefits & insurance',{T:[13334526.47,14420159.22,15404494.1,16281536.44,16767540,17551285]})
add('Debt service — General Fund','debt-service-bonds-interest','Debt',{'General Fund debt service':[5440509.32,5484902.78,5091123.52,5396418.5,5060178,6050413.63]},'General Fund only. Water/Sewer debt excluded. Flat forward placeholder until debt schedule is entered.')
base='https://city-medford-ma-budget-book.cleargov.com/21444/fund-summaries/general-fund'
add('Schools','school','Schools',{'School appropriation':[63151058.3,68872609.46,71364839.66,80199895.69,85490000,89100000]},'General Fund school amount; do not add school detail again. City-paid benefits appear separately.')
rows[-1]['url']=base
add('State assessments','state-assessments','State assessments',{'State assessments':[12300600,12072425,12483520,13184478,13623646,14137698]})
rows[-1]['url']=base
func={
'School':[63151058.3,68872609.46,71364839.66,80199895.69,85490000,89100000],
'Benefits and Insurance':[38212184.56,40433956.98,42950971.38,45712723.16,48915540,52847485],
'Public Safety':[28042954.23,27640513.02,28909503.89,29980913.47,31298731,33913827.69],
'Public Works':[14693569.72,14735553.65,15864328.07,16143843.51,19496992,20597903.24],
'State Assessments':[12300600,12072425,12483520,13184478,13623646,14137698],
'General Government':[6755863.22,7164261.4,9729509.71,8976762.82,10000847,10451506.46],
'Debt':[5440509.32,5484902.78,5091123.52,5396418.5,5060178,6050413.63],
'Culture and Recreation':[2076957.07,2366107.97,2655729.5,2912582.69,2916690,3148592.48],
'Health and Human Services':[1518681.19,1345052.14,1280738.18,1477574.53,1740263,1840506.53],
'Community Development':[502077.73,481295.35,780450.92,787526.49,933263,886805.83],
'Transfers':[None,2985342.38,14000000,18723413.07,0,0]}
rev={'Property Taxes':[127386861,130896048.48,138548478.63,152135114.67,159544213.75,166979208.1], 'State Aid':[27297415.52,28755762.02,33806036.06,34409498,35692612,36619571], 'Local Receipts':[19108568.81,22619372.77,25116961.17,26916016.96,22525100,25574600], 'Transfers In':[8788157.95,9596055.64,2086932.17,3381204.97,2711121.56,2968358.4], 'Federal Aid':[182052.33,361074.35,214842.18,186715.49,None,185000], 'Law':[35,240,975,1562.5,None,None], 'Misc. Revenue':[None,None,None,9814.4,None,None]}
summary={'actualRevenue':[182763090.61,192228553.26,199774225.21,217039926.99,163922850.01,None],'actualExpenditure':[172694455.34,183582020.13,205110714.83,223496131.93,167123657.92,None],'budgetRevenue':[180525112,181413170,194280198,203641839.87,220473047.31,232326737.5],'budgetExpenditure':[165291209,188077071.65,193223655.91,202436327,219476150,232974738.86]}
for d in rows:
 for i,a in enumerate(d['accounts']):
  a['id']=d['id']+'-'+str(i)
  a['driver']='insurance' if d['id']=='insurance' else 'pension' if d['id']=='pensions' else 'schools' if d['id']=='school' else 'debt' if d['id']=='debt-service-bonds-interest' else 'assessments' if d['id']=='state-assessments' else 'wages' if a['name'].startswith('Personnel') else 'operating'
  a['prime_account_code']=None
 d['included']=d['group']!='Separate fund' and any(a['values'][5] is not None for a in d['accounts'])
modelTotal=round(sum(a['values'][5] or 0 for d in rows if d['included'] for a in d['accounts']),2)
data=dict(version='2026-10-16-v1',retrieved='2026-10-16',sourceUpdated='2026-06-25',source=base,years=list(range(2022,2028)),basis=['Published actual']*4+['Published budget']*2,departments=rows,functions=func,revenues=rev,summary=summary,modelTotal=modelTotal,publishedTotal=232974738.86,reconciliationDifference=round(232974738.86-modelTotal,2),status='Research preview: published FY27 book, not reconciled adopted appropriations')
(P/'budget.json').write_text(json.dumps(data,indent=2))
(P.parent/'data.js').write_text('window.BUDGET_DATA = '+json.dumps(data)+';\n')
with (P/'records.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['year','basis','department','source_account_category','prime_account_code','amount','source_url','source_updated','retrieved','review_status'])
 for d in rows:
  for a in d['accounts']:
   for i,v in enumerate(a['values']):w.writerow([2022+i,data['basis'][i],d['name'],a['name'],'',v,d['url'],data['sourceUpdated'],data['retrieved'],'Transcribed; adoption/crosswalk pending'])
print('Departments',len(rows),'records',sum(len(d['accounts'])*6 for d in rows),'model',modelTotal,'difference',data['reconciliationDifference'])
