import requests as rq
import json

h = {'user-key' :'1c8025310973610801fe1f1b76b57d1c'}
h736r = rq.get('https://developers.zomato.com/api/v2.1/restaurant?res_id=18241524', headers = h)
h736rs = h736r.json()
if h736rs['is_table_reservation_supported'] == 1:
    print('yes')