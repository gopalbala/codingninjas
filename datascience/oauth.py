import requests
import json

data = {}
data = {'client_id' : '91c90ffe4e6878545407', 'state' : 'state123', 
        'redirect_uri' : 'https://www.google.com',
        'scope' : 'repo'}
response = requests.get('https://github.com/login/oauth/authorize', params = data)

print(response.url)

