

import mod_init

#driver = init.pony_driver_init()
#init.test_enter(driver)
#init.menu_button_click(driver)
#init.test_creategroup(driver)
#init.test_deletegroup(driver)
#init.test_exit(driver)

def test_10():
    driver = mod_init.pony_driver_init()
    mod_init.test_enter(driver)
    mod_init.menu_button_click(driver)
    mod_init.proizvodstvo_button_click(driver)
    mod_init.regist_of_events_button_click(driver)
    mod_init.pnsbs_71_button_click(driver)
    mod_init.continue_without_courier(driver)
    mod_init.nomer_object(driver)

if __name__ == "__main__":
    test_10()
