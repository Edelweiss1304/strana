import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import allure
import time
import os
from selenium.common.exceptions import StaleElementReferenceException


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless=new')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--virtual-time-budget=5000')
    options.add_argument('--disable-popup-blocking')
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Chrome(desired_capabilities=caps, options=options)
    if "--headless=new" in options.arguments:
        print("Аргумент headless=new успешно передан в опции Chrome WebDriver")
    else:
        print("Аргумент headless=new не найден в опциях Chrome WebDriver")
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def allure_attach_screenshot(request, driver):
    def save_screenshot(name):
        # Создаем абсолютный путь к файлу
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        safe_name = name.replace(":", "_").replace("/", "_")  # заменяем недопустимые символы на подчеркивание
        path = os.path.join(base_dir, "allure-results",
                            f"{safe_name}.png")  # добавляем к этому пути 'allure-results' и имя файла

        # Сохраняем скриншот и проверяем, что файл был создан
        if driver.save_screenshot(path):
            print(f"Screenshot saved at {path}")
        else:
            print(f"Failed to save screenshot at {path}")

        time.sleep(1)  # добавляем задержку
        with open(path, "rb") as f:
            allure.attach(f.read(), name=safe_name, attachment_type=allure.attachment_type.PNG)

    request.node.save_screenshot = save_screenshot
    yield


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    if report.failed:
        if hasattr(node, 'getfixturevalue'):
            driver = node.getfixturevalue("driver")
            screenshot_name = f"{node.nodeid}_{int(time.time())}.png"
            driver.save_screenshot(screenshot_name)
            allure.attach.file(screenshot_name, name="Screenshot", attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope="function", autouse=True)
def find_element_retry(driver):
    def find_element_with_retry(driver_instance, locator):
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            try:
                element = driver_instance.find_element(*locator)
                return element
            except StaleElementReferenceException:
                attempts += 1
        raise StaleElementReferenceException(f"Failed to find element {locator} after {max_attempts} attempts")

    yield find_element_with_retry



