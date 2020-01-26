from bs4 import BeautifulSoup
import requests as rq

response = rq.get('http://books.toscrape.com/')
data = BeautifulSoup(response.content,'html.parser')
books = data.find_all(class_ = 'nav nav-list')

cat = books[0].ul

for b in cat:
    if b != "\n":
        if b.a is not None:
            s = b.a.string
            s= s.replace('\n','')
            print(s.strip())