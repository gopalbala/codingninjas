import requests as rq
import json

h = {'user-key' :'1c8025310973610801fe1f1b76b57d1c'}
bbqres4km = rq.get('https://developers.zomato.com/api/v2.1/search?lat=28.698096&lon=77.140558&radius=4000&cuisines=193&sort=real_distance&order=asc', headers = h)
bbqrs4km = bbqres4km.json()
l = bbqrs4km['restaurants']
r_ar = []
for r in l:
    r_ar.append((r['restaurant']['name'],float(r['restaurant']['user_rating']['aggregate_rating']), r['restaurant']['R']['res_id'],r['restaurant']['location']['locality']))
r_ar.sort(key=lambda x:x[1],reverse=True)

for i in range(10):
    det = r_ar[i]
    print(det[0],det[1],det[2],det[3])    