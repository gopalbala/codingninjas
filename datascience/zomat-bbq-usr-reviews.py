## Open and read data file as specified in the question
## Print the required output in given format
## Open and read data file as specified in the question
## Print the required output in given format
import requests
import json 

 

header = {'user-key':'1c8025310973610801fe1f1b76b57d1c'}
data     = {'res_id':'18204820'}
r = requests.get('https://developers.zomato.com/api/v2.1/reviews',params=data,headers=header)
data  = json.loads(r.text)
reviews = data['user_reviews']
for rev_dtl in reviews: 
    review = rev_dtl['review']
    print(review['user']['name'], review['rating'], review['review_text'])