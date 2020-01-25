import requests as rq
import json
response = rq.get('https://api.github.com/repos/google/clusterfuzz/topics',headers={'Accept':'application/vnd.github.mercy-preview+json'})
python_data=json.loads(response.text)
l= python_data['names']
for s in l:
    print(s)