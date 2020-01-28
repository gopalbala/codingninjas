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
for author in sorted(authors):
    print(author)