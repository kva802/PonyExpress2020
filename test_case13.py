import mod_init


def test_10():
    driver = mod_init.pony_driver_init()
    mod_init.test_enter(driver)
    mod_init.menu_button_click(driver)
    mod_init.proizvodstvo_button_click(driver)
    mod_init.regist_of_events_button_click(driver)


if __name__ == "__main__":
    test_10()