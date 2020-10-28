import mod_init


def test_2():
    driver = mod_init.pony_driver_init()
    mod_init.test_enter(driver)
    mod_init.test_exit(driver)

if __name__ == "__main__":
    test_2()