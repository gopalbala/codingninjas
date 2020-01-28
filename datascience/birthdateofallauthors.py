import requests
from bs4 import BeautifulSoup

base_url = 'http://quotes.toscrape.com/'

authors = set()
for page in range(1,11): 
    url = base_url+'page/'+str(page)
    response = requests.get(url)
    html_data = response.text
    data = BeautifulSoup(html_data,'html.parser')
    auths = data.find_all(class_='author')
    for auth_str in auths: 
        authors.add(auth_str.string.strip())
        
DoB = {}
for author in sorted(authors):
    if author[0:1] == 'J':
        author_mod = author.replace(' ','-').replace('.-','-').replace('.','-')
        url = base_url + 'author/'+author_mod.strip()+'/'
        response = requests.get(url)
        html_data = response.text
        data = BeautifulSoup(html_data,'html.parser')
        date_of_birth = data.find(class_='author-born-date').string.strip()
        DoB[author] = date_of_birth
print(DoB)