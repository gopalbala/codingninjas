import requests as rq
import json

header = {'user-key':'1c8025310973610801fe1f1b76b57d1c'}

data = {'entity_id':104,'entity_type':'subzone','cuisines':'73','category':'6','sort':'rating','order':'desc'}
r = rq.get('https://developers.zomato.com/api/v2.1/search',params=data,headers=header)
data  = json.loads(r.text)
for res_dtl in data['restaurants']:
    res_data = res_dtl['restaurant']
    print(res_data['name'],res_data['user_rating']['aggregate_rating'], res_data['R']['res_id'])