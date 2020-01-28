import requests
from bs4 import BeautifulSoup

base_url = 'http://quotes.toscrape.com/'

for page in range(1,11): 
    url = base_url+'page/'+str(page)
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    quotes = data.find_all(class_='quote')
    for quote_str in quotes: 
        author = quote_str.find(class_='author').string
        if author == 'Albert Einstein': 
            quote = quote_str.find(class_='text').string
            print(quote)
 