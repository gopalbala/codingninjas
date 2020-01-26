from bs4 import BeautifulSoup
import requests as rq

allPages = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
            'http://books.toscrape.com/catalogue/page-4.html',
            'http://books.toscrape.com/catalogue/page-5.html',
            'http://books.toscrape.com/catalogue/page-6.html',
            'http://books.toscrape.com/catalogue/page-7.html',
            'http://books.toscrape.com/catalogue/page-8.html',
            'http://books.toscrape.com/catalogue/page-9.html',
            'http://books.toscrape.com/catalogue/page-10.html']

for url in allPages:
    response = rq.get(url)
    data = BeautifulSoup(response.text, 'html.parser')
    books = data.find_all(class_ = 'product_pod')
    for book in books:
        print(book.h3.a['title'])