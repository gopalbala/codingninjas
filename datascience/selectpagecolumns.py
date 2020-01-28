from bs4 import BeautifulSoup
import requests as rq
import re
import pandas as pd

allPages = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html']

column_names = ['Title', 'Link', 'Price', 'Quantity in Stock']
book_details = []
print(*column_names)
for url in allPages:
    response = rq.get(url)
    data = BeautifulSoup(response.text, 'html.parser')
    books = data.find_all(class_ = 'product_pod')
    for book in books:
        base_url = 'http://books.toscrape.com/catalogue/'
        b1_url = base_url + book.h3.a['href']
        # print(b1_url)
        rsp = rq.get(b1_url)
        # print(rsp.content)
        data1 = BeautifulSoup(rsp.content, 'html.parser')
        title = data1.find(class_='col-sm-6 product_main')
        title = data1.h1.string
        price = data1.find(class_ = 'price_color').string
        qty = data1.find(class_ = 'instock availability')
        qty = qty.contents[-1].strip()
        qty = int(re.search('\d+', qty).group())
        price = float(re.search('[\d.]+', price).group())  
        book_details.append([title, b1_url, price, qty])
        print(title,b1_url,price,qty)
        
df = pd.DataFrame(book_details, columns = ["Title", "Link", "Price", "Quantity_in_stock"])
df.to_csv('books.csv')


        # print(title,b1_url,price,qty)
        # df.to_csv('books.csv')
        
        # stck = book.find(class_="instock availability")
        # av = stck.text
        # if av is not None:
        #     av = av.replace('\n','').strip()
        # prc = book.find(class_="price_color")
        
        # print(book.h3.a['title'], prc.text,av)