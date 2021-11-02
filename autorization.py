import requests
import json
import pathes


def autorisation():
    headers = {'Content-Type': 'application/x'}
    data = {'username': pathes.login,
            'password': pathes.password,
            'grant_type': 'password',
            'scope': '',
            'client_id': '',
            'client_secret': ''}

    url = "http://"

    r = requests.post(url, data=data, headers=headers)
    answer = json.loads(r.text)
    return answer["access_token"]


if __name__ == "__main__":
    tok = autorisation()
