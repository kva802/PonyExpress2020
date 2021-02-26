import allure
import requests
import json
import pathes
import autorization
import pytest
import allure_pytest

'''
Нажать кнопку «Menu»  и выпавшем списке выбрать пункт «Производство» – «Регистрация событий» –  «71. Прибыл на склад (без сортировки)»
Нажать кнопку «Продолжить без курьера»
В поле ввода «Номер объекта» ввести текст «11-1111-1111» и нажать кнопку Enter
'''


def test_req_number_of_object():
    with allure.step('регистрация объекта'):
        try:
            tok = autorization.autorisation()
            url = 'http://events-backend-edu.pegasus.ponyex.local/api/v1/pegasus-events71/post-item'
            data = {"scannedNumber": "11-1111-1111",
                    "hostName": "abcde",
                    "eventBlockId": "356d56a1-6902-4ec4-b87c-08d8bec28892",
                    "pointId": "07c5c96a-6f52-428d-9332-0004c296067e"}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer ' + tok}
            r = requests.post(url, data=json.dumps(data), headers=headers)
            answer = json.loads(r.text)
            assert answer['metadata']['message'] == '$_OBJECT_NUMBER_NOT_VALID_$', 'номер объекта не валидный'
            assert answer['metadata']['message'] == '$_MARK_IS_NOT_BOUND_$', 'Марка не привязана'
            print(answer)
        except:
            print('ошибка')


if __name__ == "__main__":
    test_req_number_of_object()
