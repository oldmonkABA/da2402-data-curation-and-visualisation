import requests
import time
import json
import pandas as pd
import random
from concurrent.futures import ThreadPoolExecutor
def get_proxy():
    df=pd.read_html('http://www.sslproxies.org/')[0]
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    df=df[df['Https']=='yes']
    proxy_data=json.loads(df.to_json(orient='records'))
    #print(proxy_data,len(proxy_data))
    s=requests.session()
    url='https://www.nseindia.com'
    proxy_num=0
    while proxy_num<len(proxy_data):
        try:
            #proxy_num=random.randint(0, len(proxy_data))
            proxies={'https':f'http://{proxy_data[proxy_num]["IP Address"]}:{proxy_data[proxy_num]["Port"]}'}
            
            proxies={'https':'http://49.254.146.127:28919'}
            print(proxies)
            response=s.get(url,headers=headers,proxies=proxies,timeout=10)
            print(response.status_code)
            if response.status_code==200:
                print(f'Found proxy {proxies}')
                return proxies
        except Exception as e:
            print(e)
        proxy_num+=1
    return {}

def get_index_data(index_name):
    all_data=[]
    #proxies=get_proxy()
    sleep=random.randint(10,25)
    print(f'Sleeping for {sleep} seconds before Starting for {index_name}')
    time.sleep(sleep)
    for year in range(2000,2026):
        inner_payload={'name':index_name,'startDate':f'01-Jan-{year}','endDate':f'31-Dec-{year}','indexName':'NIFTY 100'}
        #payload={"cinfo":"{'name':'NIFTY 100','startDate':'01-Jan-2024','endDate':'31-Dec-2024','indexName':'NIFTY 100'}"}
        payload={"cinfo":str(inner_payload)}
        headers={"host":"www.niftyindices.com",
        "origin":"https://www.niftyindices.com",
        "referer":"https://www.niftyindices.com/reports/historical-data",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        url='https://www.niftyindices.com/Backpage.aspx/getHistoricaldatatabletoString'
        #print(payload,proxies)
        print(payload)
        try:
            reponse=requests.post(url,headers=headers,json=payload,timeout=10)
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
    return all_data


def main():
    get_proxy()
    exit()
    indices=['NIFTY 100','NIFTY 50']
    max_workers = 2  # Number of concurrent threads (adjust based on your system and target website)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Map the scraping function to the list of URLs
        results = list(executor.map(get_index_data, indices))
    #all_data=get_index_data('NIFTY 100')
    for i in range(len(results)):
        df=pd.DataFrame(results[i])
        df['HistoricalDate']=pd.to_datetime(df['HistoricalDate'])
        print(df)
        df.to_csv(f'{indices[i]}.csv',index=None)

main()