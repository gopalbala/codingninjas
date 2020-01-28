import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

 

url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'
response = requests.get(url)
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
images = data.find_all('img')
maxarea = 0 
source = ' '
for image in images: 
    if image['width'] is None or image['height'] is None: 
        continue
    area = int(image['width'])*int(image['height'])
    if area > maxarea:
        source = image['src']
        maxarea = area
print(source)