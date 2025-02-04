from selenium import webdriver


def test_basic_service():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)

    driver.quit()


def test_driver_location(chromedriver_path):
    service = webdriver.ChromeService(executable_path=chromedriver_path)

    driver = webdriver.Chrome(service=service)

    driver.quit()


def test_driver_port():
    service = webdriver.ChromeService(port=1234)

    driver = webdriver.Chrome(service=service)

    driver.quit()
