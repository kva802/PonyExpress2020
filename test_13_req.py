import autorization
import event_79_request
import allure
import pytest



def test_request_13():
    with allure.step('тест13'):
        token = autorization.autorisation()
        destinationPointId = "4110acc0-137f-4fe6-bf69-50ee2590ded4"
        r = event_79_request.included_in_consolidation(token, destinationPointId)

        if r == 'ERROR':
            print('Тест 13 не пройден')
            assert 0
            #return

        destinationPoint = r['result']['destinationPoint']

        if destinationPoint['code'] == '1202':
            print('Блок успешно создан')
            print('Тест 13 пройден')
            return
        else:
            print('Попал в другой блок')
            print('Тест 13 не пройден')
            return


if __name__ == "__main__":
    test_request_13()
