import requests
import json
import pathes
import autorization
"""
urls = [
    'http://configurations-backend-edu.pegasus.ponyex.local/',
    'http://couriers-backend-edu.pegasus.ponyex.local/',
    'http://delivery-edu.pegasus.ponyex.local/',
    'http://delivery-backend-edu.pegasus.ponyex.local/',
    'http://enumerations-backend-edu.pegasus.ponyex.local/',
    'http://events-edu.pegasus.ponyex.local/',
    'http://events-backend-edu.pegasus.ponyex.local/',
    'http://geography-edu.pegasus.ponyex.local/',
    'http://geography-backend-edu.pegasus.ponyex.local/',
    'http://localizations-backend-edu.pegasus.ponyex.local/',
    'http://organization-backend-edu.pegasus.ponyex.local/',
    'http://warehouses-edu.pegasus.ponyex.local/',
    'http://warehouses-backend-edu.pegasus.ponyex.local/',
    'http://waybills-backend-edu.pegasus.ponyex.local/'
]
swagger_tail = 'api/manual/index.html'
swagger_urls = []
for url in urls:
    swagger_urls.append(url + swagger_tail)
"""
"""
    swagger_urls =[
     'http://configurations-backend-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://couriers-backend-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://delivery-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://delivery-backend-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://enumerations-backend-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://events-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://events-backend-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://geography-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://geography-backend-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://localizations-backend-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://organization-backend-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://warehouses-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://warehouses-backend-edu.pegasus.ponyex.local/api/manual/index.html',
     'http://waybills-backend-edu.pegasus.ponyex.local/api/manual/index.html'
    ]
"""

tok = autorization.autorisation()

r1 = requests.get(pathes.urls[0] + 'api/v1/configurations/get-all', headers = {'Authorization': 'Bearer ' + tok})


id_ = '359afb0c-b870-4610-9233-524db1d5a029'
r2 = requests.get(pathes.urls[1] + f'/api/v1/couriers/get-courier-by-id/ {id_}', headers = {'Authorization': 'Bearer ' + tok, "id": id_})
print(r2.status_code)
answer = json.loads(r2.text)['result']
print(answer['firstName'] + ' ' + answer['lastName'])

r3 = requests.get(pathes.urls[1] + '/api/v1/couriers/get-couriers', headers = {'Authorization': 'Bearer ' + tok, "id": id_})
