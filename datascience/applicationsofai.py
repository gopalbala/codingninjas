import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd

 

url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'
response = requests.get(url)
html_data = response.text
data = BeautifulSoup(html_data,'html.parser')
out = data.find(class_='toclevel-1 tocsection-35')
applications = out.find_all(class_='toctext')
for i in range(1,len(applications)): 
    application = applications[i].string
    print(application)