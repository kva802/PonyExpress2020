from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import allure
import pathes


def pony_driver_init():
    with allure.step('инициализация'):
        driver = webdriver.Chrome(executable_path=pathes.driver_path)
        driver.get(pathes.url_path)
        try:
            title = WebDriverWait(driver, 10).until(EC.title_is('Пегас'))
        except:
            driver.close()
            assert 0, 'не заходит на сайт пони'
        return driver


def test_enter(driver):
    with allure.step('вход на сайт'):
        try:

            element_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
            element_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
            enter_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "css-1hnkt5t")))

        except:
            driver.close()
            assert 0, 'не найдены поля для ввода пользователя и пароля'

        element_login.send_keys(pathes.login)
        element_password.send_keys(pathes.password)
        enter_button.click()

        try:
            elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section")))
            elem.text == 'Главная страница'
            # time.sleep(5)
        except:
            driver.close()
            assert 0, 'неверный логин или пароль'


def test_exit(driver):
    with allure.step('выход с сайта'):
        try:
            exit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                            "/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]/span")))
            exit_button.click()
        except:
            driver.close()
            assert 0, 'не выполнен выход'


def menu_button_click(driver):
    with allure.step('нажать на кнопку меню'):
        try:
            menu_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/section[1]/div/div/span/span/button")))
            menu_button.click()
        except:
            driver.close()
            assert 0, 'не найдена кнопка menu'


def servis_button_click(driver):
    with allure.step('нажать на кнопку servis'):
        try:
            servis_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                              "/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/span/a")))
            servis_button.click()
        except:
            driver.close()
            assert 0, 'не найдена кнопка servis'


def uprav_button_click(driver):
    with allure.step('нажать на кнопку управление разрешениями'):
        try:
            uprav_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                             "/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/span/a")))

            uprav_button.click()
        except:
            driver.close()
            assert 0, 'не найдена кнопка управление разрешениями'


def groups_button_cick(driver):
    with allure.step('нажать на кнопку редактирование групп пользователей'):
        try:
            groups_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                              "/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/div/div/div/div/ul/li[1]/a")))
            groups_button.click()

            elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section/div")))
            elem.text == 'Редактирование групп пользователей'
        except:
            driver.close()
            assert 0, 'не открылась страница редактирования групп пользователей'


def test_creategroup(driver, name_of_group):
    with allure.step('создание группы'):
        try:
            create_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                              "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]")))
            create_button.click()

            elem_group_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/div/input")))
            elem_group_name.send_keys(name_of_group)
        except:
            print('не открылась форма для заполнения')
            driver.close()

        try:
            save_name_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button[1]")))

            save_name_button.click()

            # time.sleep(5)
            elem_find_g = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[2]/div/div/div/input")))
            elem_find_g.send_keys(name_of_group)

            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]"))).text == name_of_group
            print('группа создана')
        except:
            driver.close()
            assert 0, 'группа не создана'


def test_deletegroup(driver, name_of_group):
    with allure.step('удаление группы'):
        try:
            elem_find_g = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                            "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[2]/div/div/div/input")))
            elem_find_g.send_keys(name_of_group)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/label/span"))).click()
            delete_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                              "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[4]")))
            delete_button.click()
        except:
            driver.close()
            assert 0, 'группа не удалена'


def proizvodstvo_button_click(driver):
    with allure.step('нажать на кнопку производство'):
        try:
            proizvodstvo_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/span/a")))
            proizvodstvo_button.click()
        except:
            driver.close()
            assert 0, 'кнопка производство не найдена'


def regist_of_events_button_click(driver):
    with allure.step('нажать на кнопку регистрация событий'):
        try:
            regist_of_events_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/span/a")))

            regist_of_events_button.click()
        except:
            driver.close()
            assert 0, 'кнопка регистрация событий не найдена'


def pnsbs_71_button_click(driver):
    with allure.step('нажать на кнопку 71.Прибыл на склад (без сортировки) не найдена'):
        try:
            pnsbs_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                           "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[1]/a")))
            pnsbs_button.click()
            time.sleep(2)
            driver.switch_to_window(driver.window_handles[1])
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/h4"))).text == 'Ввод данных о блоке'
        except:
            driver.close()
            assert 0, 'кнопка 71.Прибыл на склад (без сортировки) не найдена, не открылось окно Ввод данных о блоке'


def continue_without_courier(driver):
    with allure.step('нажать на кнопку продолжить без курьера'):
        try:

            cwc_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/button[2]")))

            cwc_button.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            "/html/body/div[1]/section/section[2]/section/section/div[1]/h1"))).text == '71. Прибыл на склад (без сортировки)'
        except:
            driver.close()
            assert 0, 'кнопка Продолжить без курьера не найдена, не открылась форма 71. Прибыл на склад (без ' \
                      'сортировки) '


def number_of_object(driver, number_of_object):
    with allure.step('ввести номер объекта'):
        try:
            elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                   "/html/body/div[1]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[3]/form/input")))
            elem.send_keys(number_of_object)
            elem.send_keys('\n')
            if elem.get_attribute('style') == 'background-color: rgb(194, 48, 48);':
                print('err')
            # time.sleep(5)
        except:
            driver.close()
            assert 0, 'не найдено поле для ввода номера объекта'
        try:

            if (WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/span"))).text == '$_MARK_IS_NOT_BOUND_$'):
                print('Марка не привязана')
            elif (WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                  "/html/body/div[2]/div/div/span"))).text == f'$_OBJECT_NUMBER_NOT_VALID_$: {number_of_object}'):
                print('номер объекта не валидный')
            driver.close()
        except:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            "/html/body/div[1]/section/section[2]/section/section/div[2]/div[4]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/p"))).text == number_of_object


def vvk_79_button_click(driver):
    with allure.step('нажать на кнопку блок событий 79'):
        try:
            elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                   "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[4]/a")))
            elem.click()
            time.sleep(2)
            driver.switch_to_window(driver.window_handles[1])
            time.sleep(5)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/h4/span"))).text == 'Точка назначения'
        except:
            driver.close()
            assert 0, 'не открылась форма Точка назначения'


def select_and_find_79(driver, name_of_destination):
    with allure.step('открыть форму Выберите точку назначения'):
        try:
            select_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/button")))
            select_button.click()
            find_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/input")))
            find_button.send_keys(name_of_destination)
        except:
            driver.close()
            assert 0, 'не открылась форма Выберите точку назначения'
        try:

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            "/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[2]"))).text == name_of_destination
        except:
            driver.close()
            assert 0, 'нет точки назначения под таким номером'


def add_79(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        "/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/label/span"))).click()
        add_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[1]")))
        add_button.click()
        dalee_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button")))
    except:
        print('не открылась форма «Точка назначения» с выбранной точкой')
        driver.close()
    try:
        dalee_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        "/html/body/div[1]/section/section[2]/section/section/div[1]/h1"))).text == '79. Включен в консолидацию'
    except:
        print('не открылась форма «79. Включен в консолидацию» с номером созданного блока и точкой назначения')
        driver.close()


if __name__ == "__main__":
    driver = pony_driver_init()
    test_enter(driver)
    test_exit(driver)
