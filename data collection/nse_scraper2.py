import pandas as pd
import requests
import ssl
import json
import time

def get_nse_data():
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Step 1: Get main page to establish session
    session.get('https://www.nseindia.com', headers=headers)
    time.sleep(2)

    # Step 2: Get indices page 
    session.get('https://www.nseindia.com/reports-indices-historical-index-data', headers=headers)
    time.sleep(2)

    year=2014
    all_data=[]
    for year in range(2014,2025):
        #api_url = f'https://www.nseindia.com/api/historical/indicesHistory?indexType=NIFTY%2050&from=01-01-{year}&to=01-01-{year+1}'
        api_url=f'https://www.nseindia.com/api/historical/indicesHistory?indexType=NIFTY%2050&from=01-01-{year}&to=01-01-{year+1}'
        #print(f"Starting year {year}\n{api_url}")
        print(api_url)
        try:
            response = session.get(api_url, headers=headers, timeout=30)
            data=response.json()
            nse_data=data["data"]["indexCloseOnlineRecords"]
            all_data.extend(nse_data)
        except Exception as e:
            print(e)
        time.sleep(2)
    return all_data

def main():
    data = get_nse_data()
    df=pd.DataFrame(data)
    df.to_csv('nifty50_data.csv',index=None)
    print(data)

main()