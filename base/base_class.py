from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver

    # Открытие url с использованием переданного драйвера
    @classmethod
    def open_page(cls, driver, url):
        driver.get(url)

    @classmethod
    def get_element_visibility(cls, driver, locator, timeout=20):
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

    @classmethod
    def get_element_clickable(cls, driver, locator, timeout=20):
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

    @classmethod
    def get_s_link_wrapper_locator(cls, index):
        base_locator = "(//div[@class='s-link__wrapper'])"
        return f"{base_locator}[{index}]"
    