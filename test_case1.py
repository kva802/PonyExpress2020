import mod_init


def test_1():
    driver = mod_init.pony_driver_init()
    mod_init.test_enter(driver)

if __name__ == "__main__":
    test_1()