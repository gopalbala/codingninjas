from bs4 import BeautifulSoup

html = '<!DOCTYPE html><html><head><title>Navigate Parse Tree</title></head>\
<body><h1>This is your Assignment</h1><a href = "https://www.google.com">This is a link that will take you to Google</a>\
<ul><li><p> This question is given to test your knowledge of <b>Web Scraping</b></p>\
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web.</p></li>\
<li id = "li2">This is an li tag given to you for scraping</li>\
<li>This li tag gives you the various ways to get data from a website\
<ol><li class = "list_or">Using API of the website</li><li>Scrape data using BeautifulSoup</li><li>Scrape data using Selenium</li>\
<li>Scrape data using Scrapy</li></ol></li>\
<li class = "list_or"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">\
Clicking on this takes you to the documentation of BeautifulSoup</a>\
<a href="https://selenium-python.readthedocs.io/" id="anchor">Clicking on this takes you to the documentation of Selenium</a>\
</li></ul></body></html>'

data = BeautifulSoup(html,'html.parser')
for tag in data.find_all():
    if tag.get('id') is not None:
        print(tag.name)