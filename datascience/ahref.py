from bs4 import BeautifulSoup
import requests

html = '<!DOCTYPE html><html><head><title>Learning Beautiful Soup</title></head>\
<body><h1> About Us </h1><div class = "first_div"><p>Coding Ninjas Website</p>\
<a href="https://www.codingninjas.in/">Link to Coding Ninjas Website</a>\
<ul><li>This</li><li>is</li><li>an</li><li>unordered</li><li>list.</li></ul>\
</div><p id = "template_p">This is a template paragraph tag</p>\
<a href = "https://www.facebook.com/codingninjas/">\
This is the link of our Facebook Page</a></body></html>'

data = BeautifulSoup(html,'html.parser')
li = data.find_all('a')
for l in li:
    print(l['href'])