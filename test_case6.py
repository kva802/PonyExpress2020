import mod_init


def test_6(name_of_group):
    driver = mod_init.pony_driver_init()
    mod_init.test_enter(driver)
    mod_init.menu_button_click(driver)
    mod_init.servis_button_click(driver)
    mod_init.uprav_button_click(driver)
    mod_init.groups_button_cick(driver)
    mod_init.test_creategroup(driver, name_of_group)
    mod_init.test_deletegroup(driver, name_of_group)

if __name__ == "__main__":
    test_6('1234')