import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver_path = r'C:\Users\Арина\Downloads\chromedriver.exe'

def pony_driver_init(driver_path):
    driver = webdriver.Chrome(executable_path = driver_path)
    driver.get("http://pegasus-edu.pegasus.ponyex.local/")
    try:
        title = WebDriverWait(driver, 10).until(EC.title_is('Пегас'))
    except:
        print('не заходит на сайт пони')
        driver.close()
    return driver

def test_enter(driver_path):
    try:
        driver = pony_driver_init(driver_path)

        element_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
        element_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        enter_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-1hnkt5t")))

    except:
        print('не найдены поля для ввода пользователя и пароля')
        driver.close()

    element_login.send_keys('ext.mgu_education')
    element_password.send_keys('rg#P5hZm4F')
    enter_button.click()

    try:
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section")))
        elem.text == 'Главная страница'
        time.sleep(5)
    except:
        print('неверный логин или пароль')
        driver.close()
    return driver
    #elem = driver.find_element_by_xpath("/html/body/div[1]/section/section[2]/section")
    #elem.text == 'Главная страница'

def test_exit(driver_path):

    driver = test_enter(driver_path)

    try:
        exit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                      "/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]/span" )))
        #exit_button = driver.find_element_by_xpath("/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]/span")
        exit_button.click()
        time.sleep(5)
        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "login")))
    except:
        print('не выполнен выход')
        driver.close()

    #time.sleep(5)

    #driver.close()
def test_56(driver_path):
    driver = test_enter(driver_path)
    try:
        menu_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/section/section[1]/div/div/span/span/button")))
        menu_button.click()
    except:
        print('не найдена кнопка menu')
        driver.close()

    try:
        servis_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                           "/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/span/a")))
        servis_button.click()

        uprav_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          "/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/span/a")))

        uprav_button.click()

        #
    except:
        print('не найдена кнопка servis')
        driver.close()

    try:
        groups_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          "/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/div/div/div/div/ul/li[1]/a")))
        groups_button.click()

        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section/div")))
        elem.text == 'Редактирование групп пользователей'

        time.sleep(5)
    except:
        print('не открылась страница редактирования групп пользователей')
        driver.close()

    try:
        create_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]")))
        create_button.click()

        elem_group_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,"bp3-form-content")))
    except:
        print('не открылась форма для заполнения')
        driver.close()

    try:
        save_name_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,"bp3-button bp3-intent-primary css-glsl4t")))


        elem_group_name.send_keys('1234')

        save_name_button.click()

        time.sleep(5)
        #elem_find_g = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[2]/div/div/div/input")))
        #elem_find_g.send_keys('1234')

        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]"))).text == '1234'

    except:
        print('группа не создана')
        driver.close()

if __name__ == "__main__":
    driver_path = r'C:\Users\Арина\Downloads\chromedriver.exe'
    test_56(driver_path)