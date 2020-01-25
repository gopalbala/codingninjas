import requests as rq
import json

h = {'user-key' :'1c8025310973610801fe1f1b76b57d1c'}
lr = rq.get('https://developers.zomato.com/api/v2.1/geocode?lat=28.627&lon=77.2166', headers = h)
lrs = lr.json()
print(lrs['location']['entity_id'], lrs['location']['entity_type'])