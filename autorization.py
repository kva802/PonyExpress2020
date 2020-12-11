import requests
import json
import pathes

def autorisation():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'username': pathes.login,
              'password': pathes.password,
              'grant_type': 'password',
              'scope': 'pegasus',
              'client_id': 'pegasus-v2',
              'client_secret': 'secret'}

    url = "http://srv-pnew-01-test:1001/auth/connect/token"

    r = requests.post(url, data = data, headers = headers)
    answer = json.loads(r.text)
    return(answer["access_token"])

if __name__ == "__main__":
    tok = autorisation()