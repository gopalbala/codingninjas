import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

 

url1 = 'https://www.imdb.com/search/title/?release_date='
url2 = '&sort=num_votes,desc&page=1&ref_=adv_nxt'
for year in range(2010,2015):
    url = url1 + str(year) + url2 
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    out = data.find(class_='lister-item mode-advanced')
    title = out.h3.a.string
    print(title)