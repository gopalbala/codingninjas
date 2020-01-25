import requests as rq
import json

# 'Authorization' : 'token bc21b964a90af03261460cd3fe7777cac7833a6f', 

h = {'Accept' :'application/vnd.github.baptiste-preview+json' }
response = rq.get('https://api.github.com/repos/CodingNinjasCodes/JSNotes/stats/contributors',headers=h)
members = response.json()
for t in members:
    print(t['author']['login'],t['total'])
    

# r = requests.get('https://api.github.com/repos/CodingNinjasCodes/JSNotes/stats/contributors',auth=('Senthilmano81',access_token))
# print(r.status_code)
# data = json.loads(r.text)
# data[2]
# for contributor in data:
#     print(contributor['author']['login'],contributor['total'])