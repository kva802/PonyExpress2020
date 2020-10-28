import mod_init


def test_5():
    driver = mod_init.pony_driver_init()
    mod_init.test_enter(driver)
    mod_init.menu_button_click(driver)
    mod_init.servis_button_click(driver)
    mod_init.uprav_button_click(driver)
    mod_init.groups_button_cick(driver)

if __name__ == "__main__":
    test_5()