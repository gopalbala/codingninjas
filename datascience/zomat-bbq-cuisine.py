## Open and read data file as specified in the question
## Print the required output in given format
import requests as rq
import json

h = {'user-key' :'1c8025310973610801fe1f1b76b57d1c'}
response = rq.get('https://developers.zomato.com/api/v2.1/cuisines?city_id=1', headers = h)
rs = response.json()
cusines = rs['cuisines']
for cus in cusines:
    if cus['cuisine']['cuisine_name'] == 'BBQ':
        print(cus['cuisine']['cuisine_id'])
        break