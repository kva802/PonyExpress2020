import mod_init

def test_11():
    driver = mod_init.pony_driver_init()
    mod_init.test_enter(driver)
    mod_init.menu_button_click(driver)
    mod_init.proizvodstvo_button_click(driver)
    mod_init.regist_of_events_button_click(driver)
    mod_init.pnsbs_71_button_click(driver)
    mod_init.continue_without_courier(driver)
    mod_init.number_of_object(driver, '0012345666')


if __name__ == "__main__":
    test_11()
