import requests
import json

d = {'code' : '8602edb35e618702c039', 
     'redirect_uri' : 'https://www.google.com', 'state' : 'state123', 'client_id' : '91c90ffe4e6878545407',
    'client_secret' : '3c1edaf5fb7f51b45d4458c6bf7cd754a753ef3e'} 

response = requests.post('https://github.com/login/oauth/access_token', data = d)
print(response.text)