import json
import pathes
import autorization
import requests


def ad_ID_3():
    try:
        tok = autorization.autorisation()
        addressId = '2344f4b3-a7bd-4512-686d-08d8c4533103'
        url = f'http://geography-backend-edu.pegasus.ponyex.local/api/v1/geography/get-polygon-with-coordinates-by-address-id/{addressId}'
        data = {"addressId": "2344f4b3-a7bd-4512-686d-08d8c4533103"}
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + tok}
        r = requests.get(url, params=json.dumps(data), headers=headers)
        answer = json.loads(r.text)
        if '$_ADDRESS_NOT_FOUND_$' in str(answer['metadata']['message']):
            print('адреса с таким айди нет')
        print(answer)
    except:
        print('ошибка')


if __name__ == "__main__":
    ad_ID_3()