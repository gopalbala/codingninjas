import requests as rq
import json

# 'Authorization' : 'token bc21b964a90af03261460cd3fe7777cac7833a6f', 

# h = {'Accept' :'application/vnd.github.baptiste-preview+json','type' : 'all'}
# response = rq.get('https://api.github.com/orgs/fossasia/repos?type=all&per_page=500',headers=h)
# repos = response.json()
# print(len(repos))
l = []
for i in range(1,5):
    h = {'Accept' :'application/vnd.github.baptiste-preview+json','type' : 'all'}
    response = rq.get('https://api.github.com/orgs/fossasia/repos?type=public&per_page=100&page='+str(i))
    if response.text is not None and response.text != '':
        repos = response.json()
        for rep in repos:
            l.append(rep['name'])
    else:
        break

print(len(l))
for i in l:
    print(i)


# for i in range(1,data['public_repos']//30 +2,1):
#     res = requests.get("https://api.github.com/orgs/fossasia/repos", headers = h,
#                       params = {'type': 'all', 'page' : i})