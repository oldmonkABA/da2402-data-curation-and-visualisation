import requests
import time
import json
import pandas as pd
headers={"host":"www.niftyindices.com",
"origin":"https://www.niftyindices.com",
"referer":"https://www.niftyindices.com/reports/historical-data",
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
all_data=[]
for year in range(2000,2026):
    #year=2024
    inner_payload={'name':'NIFTY 100','startDate':f'01-Jan-{year}','endDate':f'31-Dec-{year}','indexName':'NIFTY 100'}
    #payload={"cinfo":"{'name':'NIFTY 100','startDate':'01-Jan-2024','endDate':'31-Dec-2024','indexName':'NIFTY 100'}"}
    payload={"cinfo":str(inner_payload)}
    
    url='https://www.niftyindices.com/Backpage.aspx/getHistoricaldatatabletoString'
    print(payload)
    try:
        reponse=requests.post(url,headers=headers,json=payload)
        if reponse.status_code==200:
            json_data=json.loads(reponse.json()['d'])
            #print(json_data)
            #exit()
            print(f'Found {len(json_data)} records')
            if len(json_data)>0:
                all_data.extend(json_data)
    except Exception as e:
        print(e)
    time.sleep(2)
    #print(type(json_data))
df=pd.DataFrame(all_data)
print(df)
df.to_csv('nifty100.csv',index=None)