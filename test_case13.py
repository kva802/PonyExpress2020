import mod_init


def test_14():
    driver = mod_init.pony_driver_init()
    mod_init.test_enter(driver)
    mod_init.menu_button_click(driver)
    mod_init.proizvodstvo_button_click(driver)
    mod_init.regist_of_events_button_click(driver)
    mod_init.vvk_79_button_click(driver)
    mod_init.select_and_find_79(driver, '1202')
    mod_init.number_of_object(driver, '99-9999-9999/999')

if __name__ == "__main__":
    test_14()