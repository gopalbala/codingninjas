import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd


url = 'https://www.imdb.com/search/title/?release_date=2018&sort=num_votes,desc&page=1&ref_=adv_nxt'
response = requests.get(url)
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
out = data.find_all(href='#Applications')
for i in range(0,3):
    title = out[i].h3.a.string
    genre = out[i].find(class_='genre').string
    print(title+' ; '+genre)