assert 'Пегас' == driver.title

element_login = driver.find_element_by_name("login")
element_password = driver.find_element_by_name("password")
enter_button = driver.find_element_by_class_name("css-1hnkt5t")

element_login.send_keys('ext.mgu_education')
element_password.send_keys('rg#P5hZm4F')
enter_button.click()

time.sleep(5)

elem = driver.find_element_by_xpath("/html/body/div[1]/section/section[2]/section")
elem.text == 'Главная страница'

enter_button = driver.find_element_by_xpath("/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]/span")
#class="bp3-button bp3-minimal"
enter_button.click()


#driver.close()