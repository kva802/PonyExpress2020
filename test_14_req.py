import autorization
import event_79_request
import allure
import pytest
import allure_pytest


'''

'''


def test_request_14():
    with allure.step('тест13'):
        token = autorization.autorisation()

        if token == 'ERROR':
            print('Тест 14 не пройден')
            return

        destinationPointId = "4110acc0-137f-4fe6-bf69-50ee2590ded4"

        r = event_79_request.included_in_consolidation(token, destinationPointId)

        if r == 'ERROR' or r['result'] is None:
            print('Не смог создать блок событий 79 - включён в консолидацию')
            print('Тест 14 не пройден')
            return

        destinationPoint = r['result']['destinationPoint']

        if destinationPoint['code'] != '1202':
            print('Попал в другой блок')
            print('Тест 14 не пройден')
            return

        print('Блок успешно создан')

        id_ = r['result']['id']

        number = "99-9999-9999/999"

        r = event_79_request.add_object(token, id_, number)

        if r == 'ERROR':
            print('Не смог вбить номер места накладной')
            print('Тест 14 не пройден')
            return

        if r['metadata']['message'] == "$_PLACE_IS_OUT_OF_RANGE_$":
            print('Система вернула ошибку «Отсутствует введенное место накладной»')
            print('Тест 14 пройден')
            return
        else:
            print('Система нашла номер места накладной: ' + number)
            print('Тест 14 не пройден')
            return


if __name__ == "__main__":
    test_request_14()
