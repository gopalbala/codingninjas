import requests as rq
import json

h = {'user-key' :'1c8025310973610801fe1f1b76b57d1c'}
h736rwr = rq.get('https://developers.zomato.com/api/v2.1/reviews?res_id=18241524', headers = h)
h736rwrs = h736rwr.json()
l =  h736rwrs['user_reviews']
for rev in l:
    print(rev['review']['user']['name'],rev['review']['rating'],rev['review']['review_text'])
    