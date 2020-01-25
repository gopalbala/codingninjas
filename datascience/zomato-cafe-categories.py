import requests as rq
import json

header = {'user-key':'1c8025310973610801fe1f1b76b57d1c'}

r = rq.get('https://developers.zomato.com/api/v2.1/categories',headers=header)
data  = json.loads(r.text)
for cat_dtl in data['categories']:
    cat_data = cat_dtl['categories']
    if cat_data['name']=='Cafes':
        print(cat_data['id'])
 