import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

 

url1 = 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start='
url2 = '&ref_=adv_prv'
maxRunTime = 0 
title = ' ' 
for page in range(5):
    page_start = (page*50) + 1
    url = url1 + str(page_start) + url2
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    out = data.find_all(class_='lister-item mode-advanced')
    for i in range(len(out)):
        runTime = out[i].find(class_='runtime').string.split(' ')[0]
        runTime = int(runTime)
        if runTime > maxRunTime:
            title = out[i].h3.a.string    
            maxRunTime = runTime
            
print(title, maxRunTime)