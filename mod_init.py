from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import pathes

def pony_driver_init():
    driver = webdriver.Chrome(executable_path = pathes.driver_path)
    driver.get(pathes.url_path)
    try:
        title = WebDriverWait(driver, 10).until(EC.title_is('Пегас'))
    except:
        print('не заходит на сайт пони')
        driver.close()
    return driver

def test_enter(driver):
    try:

        element_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
        element_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        enter_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-1hnkt5t")))

    except:
        print('не найдены поля для ввода пользователя и пароля')
        driver.close()

    element_login.send_keys(pathes.login)
    element_password.send_keys(pathes.password)
    enter_button.click()

    try:
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section")))
        elem.text == 'Главная страница'
        #time.sleep(5)
    except:
        print('неверный логин или пароль')
        driver.close()

def test_exit(driver):


    try:
        exit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                      "/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]/span" )))
        exit_button.click()
    except:
        print('не выполнен выход')
        driver.close()

def menu_button_click(driver):

    try:
        menu_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/section/section[1]/div/div/span/span/button")))
        menu_button.click()
    except:
        print('не найдена кнопка menu')
        driver.close()

def servis_button_click(driver):
    try:
        servis_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                           "/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/span/a")))
        servis_button.click()
    except:
        print('не найдена кнопка servis')
        driver.close()

def uprav_button_click(driver):
    try:
        uprav_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          "/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/span/a")))

        uprav_button.click()
    except:
        print('не найдена кнопка управление разрешениями')
        driver.close()

def groups_button_cick(driver):
    try:
        groups_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          "/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/div/div/div/div/ul/li[1]/a")))
        groups_button.click()

        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section/div")))
        elem.text == 'Редактирование групп пользователей'
    except:
        print('не открылась страница редактирования групп пользователей')
        driver.close()

def test_creategroup(driver, name_of_group):
    try:
        create_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]")))
        create_button.click()

        elem_group_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/div/input")))
        elem_group_name.send_keys(name_of_group)
    except:
        print('не открылась форма для заполнения')
        driver.close()


    try:
        save_name_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button[1]")))

        save_name_button.click()

        #time.sleep(5)
        elem_find_g = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[2]/div/div/div/input")))
        elem_find_g.send_keys(name_of_group)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]"))).text == name_of_group
        print('группа создана')
    except:
        print('группа не создана')
        driver.close()

def test_deletegroup(driver, name_of_group):

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
        print('группа не удалена')
        driver.close()

def proizvodstvo_button_click(driver):
    try:
        proizvodstvo_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/span/a")))
        proizvodstvo_button.click()
    except:
        print('кнопка производство не найдена')
        driver.close()

def regist_of_events_button_click(driver):
    try:
        regist_of_events_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/span/a")))

        regist_of_events_button.click()
    except:
        print('кнопка регистрация событий не найдена')
        driver.close()

def pnsbs_71_button_click(driver):
    try:
        pnsbs_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[1]/a")))
        pnsbs_button.click()
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/h4"))).text == 'Ввод данных о блоке'
    except:
        print('кнопка 71.Прибыл на склад (без сортировки) не найдена, не открылось окно Ввод данных о блоке')
        driver.close()

def continue_without_courier(driver):
    try:

        cwc_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[2]/span")))

        #time.sleep(5)
        cwc_button.click()
        #time.sleep(5)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div[1]/h1"))).text == '71. Прибыл на склад (без сортировки)'
    except:
        print('кнопка Продолжить без курьера не найдена, не открылась форма 71. Прибыл на склад (без сортировки)')
        driver.close()

def number_of_object(driver, number_of_object):
    try:
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[3]/form/input")))
        elem.send_keys(number_of_object)
        elem.send_keys('\n')
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/span")))
        if elem.get_attribute('style') == 'background-color: rgb(194, 48, 48);':
            print('err')
        #time.sleep(5)
    except:
        print('не найдено поле для ввода номера объекта')
        driver.close()

def vvk_79_button_click(driver):
    try:
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[4]/a")))
        elem.click()
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/h4/span"))).text == 'Точка назначения'
    except:
        print('не открылась форма Точка назначения')
        driver.close()

def select_and_find_79(driver, name_of_destination):
    try:
        select_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/button")))
        select_button.click()
        find_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/input")))
        find_button.send_keys(name_of_destination)
    except:
        print('не открылась форма Выберите точку назначения')
        driver.close()
    try:

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[2]"))).text == name_of_destination
    except:
        print('нет точки назначения под таким номером')
        driver.close()

def add_79(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/label/span"))).click()
        add_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[1]")))
        add_button.click()
        dalee_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button")))
    except:
        print('не открылась форма «Точка назначения» с выбранной точкой')
        driver.close()
    try:
        dalee_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div[1]/h1"))).text == '79. Включен в консолидацию'
    except:
        print('не открылась форма «79. Включен в консолидацию» с номером созданного блока и точкой назначения')
        driver.close()




if __name__ == "__main__":
    driver = pony_driver_init()
    test_enter(driver)
    test_exit(driver)
