## Print the required output in given format
import requests as rq
import json
response = rq.get('https://holidayapi.com/v1/holidays?pretty&key=057ab8e3-e480-4464-aa6b-0f25923fc223&country=IN&year=2018')
python_data=json.loads(response.text)
for holiday in python_data['holidays']:
    if holiday['date']=='2018-10-02':
        print(holiday['name'])