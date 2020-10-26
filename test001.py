import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import init

#driver = init.pony_driver_init()
#init.test_enter(driver)
#init.menu_button_click(driver)
#init.test_creategroup(driver)
#init.test_deletegroup(driver)
#init.test_exit(driver)

def test_8():
    driver = init.pony_driver_init()
    init.test_enter(driver)
    init.menu_button_click(driver)
    init.proizvodstvo_button_click(driver)
    init.regist_of_events_button_click(driver)
    init.pnsbs_71_button_click(driver)
    init.continue_without_courier(driver)


if __name__ == "__main__":
    test_8()
