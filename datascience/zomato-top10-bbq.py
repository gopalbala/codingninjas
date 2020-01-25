import requests as rq
import json

h = {'user-key' :'1c8025310973610801fe1f1b76b57d1c'}
bbqres = rq.get('https://developers.zomato.com/api/v2.1/search?lat=28.698096&lon=77.140558&cuisines=193&sort=real_distance&order=asc', headers = h)
bbqrs = bbqres.json()
rsts = bbqrs['restaurants']
for r in rsts:
    print(r['restaurant']['name'],r['restaurant']['user_rating']['aggregate_rating'], r['restaurant']['R']['res_id'],r['restaurant']['location']['locality'])