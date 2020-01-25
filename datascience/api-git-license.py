import requests as rq
import json
response = rq.get('https://api.github.com/repos/google/go-cloud')
python_data=json.loads(response.text)
print(python_data['license']['name'])