import requests as rq
import json

h = {'user-key' :'1c8025310973610801fe1f1b76b57d1c'}
h736r = rq.get('https://developers.zomato.com/api/v2.1/restaurant?res_id=18241524', headers = h)
h736rs = h736r.json()
print(h736rs['user_rating']['aggregate_rating'])
print(h736rs['average_cost_for_two'])
print(h736rs['cuisines'])
print(h736rs['location']['address'])