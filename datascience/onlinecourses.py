import requests as rq
import json
url = 'https://codingninjas.in/api/v3/courses'
response = rq.get(url)
print(response.text)
python_data = json.loads(response.text)
# print(python_data['data']['courses'])
pp = python_data['data']['courses']
print(pp)
for p in pp:
    if p['available_online']:
        print(p['name'])