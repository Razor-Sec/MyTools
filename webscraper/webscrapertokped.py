import requests
import csv

url = 'https://api.bukalapak.com/multistrategy-products'
param = {
'peram'
'keywords' : 'sepatu',
'page' : 2,
'limit' : '50',
'offset' : 50,
'access_token': 'N27_v5n5noaC3LGyHznXIf-YQDUerWehJ0pul5Dz9CFyrg'
}

r = requests.get(url, params=param).json()
product = r['data']
for p in product:
    print(p)