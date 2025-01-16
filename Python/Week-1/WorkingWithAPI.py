import requests

baseUrl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

r = requests.get(baseUrl +  endpoint)

print(r.json())