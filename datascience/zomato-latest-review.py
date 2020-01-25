import requests as rq
import json

header = {'user-key':'1c8025310973610801fe1f1b76b57d1c'}
data = {'entity_id':104,'entity_type':'subzone','cuisines':'73','category':'6','sort':'rating','order':'desc'}
r = rq.get('https://developers.zomato.com/api/v2.1/search',params=data,headers=header)
data  = json.loads(r.text)
res_dtl = data['restaurants'][0]
res_id = res_dtl['restaurant']['R']['res_id']

data = {'res_id':res_id}
rev = rq.get('https://developers.zomato.com/api/v2.1/reviews',params=data,headers=header)
data = json.loads(rev.text)
reviews = data['user_reviews']
for rev_dtl in reviews: 
    review = rev_dtl['review']
    print(review['user']['name'], review['rating'], review['review_text'])