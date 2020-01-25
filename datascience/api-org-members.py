import requests as rq
import json

# 'Authorization' : 'token bc21b964a90af03261460cd3fe7777cac7833a6f', 

h = {'Accept' :'application/vnd.github.baptiste-preview+json' }
# response = rq.get('https://api.github.com/orgs/CodingNinjasCodes/repos',headers=h)
# members = response.json()
# l = []
# for t in members:
#      if t['fork'] == False:
#         l.append(t['name'])
# st = []

# for s in l:
#     url = 'https://api.github.com/repos/CodingNinjasCodes/'+s+'/contributors'
#     response = rq.get(url,headers=h)
#     if response.text is not None and response.text != '':
#         mb = response.json()
#         for t in mb:
#             st.append(t['login'])

# st1 = set(st)
# for s in st1:
#     print(s)
response = rq.get('https://api.github.com/orgs/CodingNinjasCodes/members',headers=h)
members = response.json()
for m in members:
    print(m['login'])
    