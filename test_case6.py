import mod_init


def test_6():
    driver = mod_init.pony_driver_init()
    mod_init.test_enter(driver)
    mod_init.menu_button_click(driver)
    mod_init.servis_button_click(driver)
    mod_init.uprav_button_click(driver)
    mod_init.groups_button_cick(driver)
    mod_init.test_creategroup(driver, '1234')
    mod_init.test_deletegroup(driver, '1234')

if __name__ == "__main__":
    test_6()