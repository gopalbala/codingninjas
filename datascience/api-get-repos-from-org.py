import requests as rq
import json

h = {'Authorization' : 'token bc21b964a90af03261460cd3fe7777cac7833a6f', 'Accept' :'application/vnd.github.baptiste-preview+json' }
response = rq.get('https://api.github.com/orgs/CodingNinjasCodes/repos',headers=h)
python_data=json.loads(response.text)
d = []
d = python_data
#print(len(d))

for i in range(0,len(d)):
    print(d[i]['name'],d[i]['watchers_count'],d[i]['forks_count'])
