import requests as rq
import json

h = {'Accept' : 'application/vnd.github.black-panther-preview+json'}
response = rq.get('https://api.github.com/repos/CodingNinjasCodes/SmoothScrollJs/community/profile',headers=h)
prof = response.json()     
print(prof['health_percentage'])