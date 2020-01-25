import requests as rq
import json
response = rq.get('https://api.github.com/repos/google/science-journal-ios/languages',headers={'Accept':'application/vnd.github.mercy-preview+json'})
python_data=json.loads(response.text)
d = {}
d = python_data
for k in d:
    print(k)