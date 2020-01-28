import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

def find_tags(quote):
    tag_strs = quote.find_all(class_='tag')
    tags = []
    for tag_str in tag_strs:
        tags.append(tag_str.string)
    return tags

 

base_url = 'http://quotes.toscrape.com/'

for page in range(1,11): 
    url = base_url+'page/'+str(page)
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    quotes = data.find_all(class_='quote')
    for quote_str in quotes: 
        tags  = find_tags(quote_str)
        if 'humor' in tags: 
            quote = quote_str.find(class_='text').string
            print(quote)