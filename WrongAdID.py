import requests
import json
import pathes
import autorization


def ad_ID():
    try:
        tok = autorization.autorisation()
        id_ = '2344f4b3-a7bd-4512-686d-08d8c4533103'
        url = f'http://geography-backend-edu.pegasus.ponyex.local/api/v1/addresses/get-by-id/{id_}'
        data = {"id": "2344f4b3-a7bd-4512-686d-08d8c4533103",
                "hostName": "abcde"}
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + tok}
        r = requests.get(url, params=json.dumps(data), headers=headers)
        answer = json.loads(r.text)
        if answer['metadata']['message'] == 'Object not found':
            print('адреса с таким айди нет')
        print(answer)
    except:
        print('ошибка')


if __name__ == "__main__":
    ad_ID()
