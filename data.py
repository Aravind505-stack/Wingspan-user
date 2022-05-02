import pandas as pd
import json

data = pd.read_csv("InfosysTestData.csv",sep=";") #use argparse for specifying the path
del data['region']
del data['company_code']
del data['has_managerial_role']
del data['travel_country']
del data['travel_state']
del data['travel_city']
del data['trip_start_date']
del data['trip_end_date']

j = data.to_json()
gh = json.loads(j)
j = 0
ui = []
iu = []
while(j < 100):
    for i in gh:
        iu.append(gh.get(i).get(str(j)))
    j = j+1
    ui.append(iu)
    iu = []

for i in ui:
    with open("try1.txt", "a") as trytyu:
        trytyu.write(str(i))
