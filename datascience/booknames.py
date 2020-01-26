from bs4 import BeautifulSoup
import requests as rq

response = rq.get('http://books.toscrape.com/')
data = BeautifulSoup(response.content,'html.parser')

books = data.find_all(class_ = 'product_pod')
count = 1
for book in books:
    if count <= 20:
        print(book.h3.a['title'])
    count+=1