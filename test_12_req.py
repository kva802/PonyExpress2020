import allure
import requests
import json
import pathes
import autorization
import pytest
import allure_pytest

'''
В поле ввода «Номер объекта» ввести текст «11-1111-1111» и нажать кнопку Enter
В списке объектов выбрать введенный номер «11-1111-1111» и нажать кнопку удалить
'''


def test_without_sorting_and_couriers(token):
    with allure.step('блок событий 71'):
        try:
            token = autorization.autorisation()
            url = 'http://events-backend-edu.pegasus.ponyex.local/api/v1/event-blocks71/post-item'
            headers = {'Authorization': f'Bearer {token}'}
            data = {"description": ""}

            r = requests.post(url, json=data, headers=headers)

            assert r.status_code == 200, 'успешно'
            answer = json.loads(r.text)
            id__ = answer['result']['id']
            return id__
        except:
            print('ошибка, блок не создан')


def test_add_object(token, id_, number):
    with allure.step('добавление объекта'):
        try:
            url = 'http://events-backend-edu.pegasus.ponyex.local/api/v1/pegasus-events71/post-item'
            headers = {'Authorization': f'Bearer {token}'}
            data = {
                "eventBlockId": id_,
                "pointId": "07c5c96a-6f52-428d-9332-0004c296067e",
                "scannedNumber": number,
                "hostname": "abcde"
            }

            r = requests.post(url, json=data, headers=headers)

            assert r.status_code == 200, 'успешно'
            answer = json.loads(r.text)
            waybill_id_ = answer['result']['id']
            return waybill_id_
        except:
            print('ошибка, блок не создан')


def test_find_object(token, id_):
    with allure.step('нахождение объекта'):
        url = f'http://events-backend-edu.pegasus.ponyex.local/api/v1/pegasus-events71/get-events-by-event-block-id/{id_}'
        headers = {'Authorization': f'Bearer {token}'}
        data = {'id': id_}

        r = requests.get(url, headers=headers, params=data)

        assert r.status_code != 200, 'Запрос вернул код ошибки'
        assert r.status_code == 200, 'Запрос вернул код успеха'


def test_delete_object(token, id_):
    with allure.step('удаление объекта'):
        url = f'http://events-backend-edu.pegasus.ponyex.local/api/v1/pegasus-events71/delete-item/{id_}'
        headers = {'Authorization': f'Bearer {token}'}
        data = {'id': id_}

        r = requests.delete(url, headers=headers, params=data)

        assert r.status_code != 200, 'Запрос вернул код ошибки'
        assert r.status_code == 200, 'Запрос вернул код успеха'


if __name__ == "__main__":
    token = autorization.autorisation()
    id_ = test_without_sorting_and_couriers(token)
    number = "11-1111-1111"
    waybill_id = test_add_object(token, id_, number)
    test_find_object(token, id_)
    test_delete_object(token, waybill_id)
