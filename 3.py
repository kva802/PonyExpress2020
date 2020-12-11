import requests
import json
import pathes
import autorization

'''
создание группы
проверка ее существования
удаление группы
проверка удаления
'''

def group_existence(tok):
    url = 'http://srv-pnew-01-test.ponyex.local:1001/api/v1/user-profile-groups/get-limit/1000'
    r = requests.get(url, headers = {'Authorization': 'Bearer ' + tok})
    if '"abc"' in r.text:
        return(1)
    else:
        return(0)

def test_creategroup():
    try:
        tok = autorization.autorisation()
        url = 'http://srv-pnew-01-test.ponyex.local:1001/api/v1/user-profile-groups/post-item'
        data = {'displayName': "abc"}
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + tok}
        r = requests.post(url, data = json.dumps(data), headers = headers)
        answer = json.loads(r.text)
        print(answer)
        id_ = json.loads(r.text)['result']['id']
        assert group_existence(tok) == 1
        return(id_)
    except:
        print('группа не создана')



def test_deletegroup(id_):
    try:
        tok = autorization.autorisation()
        url = 'http://srv-pnew-01-test.ponyex.local:1001/api/v1/user-profile-groups/delete-item'
        params = {'id': id_ }
        headers = {'Authorization': 'Bearer ' + tok}

        r = requests.delete(url, headers = headers, params = params)
        r.status_code == 200
        assert group_existence(tok) == 0
    except:
        print('группа не удалена')


if __name__ == "__main__":
    id_ = test_creategroup()
    test_deletegroup(id_)


