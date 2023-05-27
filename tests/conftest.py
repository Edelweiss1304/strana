import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import allure
import time
import os


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--headless")
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Chrome(desired_capabilities=caps, options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def allure_attach_screenshot(request):
    def save_screenshot(driver, name):
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


def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = node.funcargs["driver"]
        screenshot_name = f"{node.nodeid}_{int(time.time())}"
        node.save_screenshot(driver, screenshot_name)

