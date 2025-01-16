import requests # type: ignore

baseUrl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

def main_requests(baseUrl, endpoint):
    r = requests.get(baseUrl +  endpoint)
    return r.json()

def get_pages(response):
    pages = response['info']['pages']
    return pages
def parse_json(response):
    for items in response['results']:
        print(items['name'],len(items['episode']))
    return    



# print(r.json())

data = main_requests(baseUrl, endpoint)
parse_json(data)
