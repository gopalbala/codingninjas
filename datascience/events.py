import requests as rq
import json
url = 'https://codingninjas.in/api/v3/events'
response = rq.get(url)
# print(response.text)
python_data = json.loads(response.text)
pp = python_data['data']['past_registered_events']
for p in pp:
    if 'Workshop' in p['name']:
        print(p['name'])