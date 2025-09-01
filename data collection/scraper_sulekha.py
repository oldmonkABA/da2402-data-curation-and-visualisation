import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from copy import copy
#pip install lxml
url = "https://www.sulekha.com/home-cleaning-services/chennai"
response = requests.get(url)
if response.status_code==200:
    with open("sulekha.html", "w", encoding="utf-8") as f:
        f.write(response.text)


with open('sulekha.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
soup = bs(html_content, 'lxml')#html.parser,lxml,html5lib
cards = soup.find_all('div',class_="sk-card") #this gets the whole div
sulekha_data=[]
business_info={}
for card in cards:
    # Id, name
    business_info['id']=card.get('businessid',"")
    business_info['name']=card.get('businessname',"")
    
    print("businessid",card.get('businessid',""))
    print("business name",card.get('businessname',""))
    #locality
    locality = card.find('div',class_="locality")
    #print(locality)
    location = locality.find('span')
    business_info['locality']=location.get_text()
    location=locality.find('div',class_='sk-link')
    if location:
        business_info['lat']=location.get('businesslat',"")
        business_info['long']=location.get('businesslong',"")
    else:
        business_info['lat']=''
        business_info['long']=''
    #Ratings
    rating_div=card.find('div','ratings-group')
    rating=rating_div.find('b')
    if rating:
        business_info['rating']=rating.get_text()
    else:
        business_info['rating']=''
    
    #list of services
    services_div=card.find('div',class_="tags-link")
    
    services_list=services_div.find_all('spam',class_="tag-link-item")
    services=[]
    if not services_list:
        services_list=services_div.find_all('span',class_="tag-link-item") 
    for service in services_list:
        service_name=service.get_text()
        if service_name not in services:
            services.append(service_name)
    
    #print(services_list)
    business_info['services']=services

    #keypoints
    key_points=card.find('div','key-points light')
    #print(key_points)
    key_point_span = key_points.find_all('span')
    for key_point in key_point_span:
        if 'Response Time' in key_point.get_text():
            b_tag=key_point.find('b')
            business_info['response_time']=b_tag.get_text()
        if 'Sulekha score' in key_point.get_text():
            b_tag=key_point.find('b')
            business_info['sulekha_score']=b_tag.get_text()


    sulekha_data.append(copy(business_info))
    #print(business_info)
    #exit()
df=pd.DataFrame(sulekha_data)
df.to_csv('sulekha_10.csv',index=None)
