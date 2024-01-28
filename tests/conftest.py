import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
import os
import testit


class NoSSLVerificationAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        kwargs['assert_hostname'] = False
        kwargs['cert_reqs'] = 'CERT_NONE'
        self.poolmanager = PoolManager(*args, **kwargs)


# Глобальная фикстура для отключения SSL верификации
@pytest.fixture(autouse=True, scope='session')
def no_ssl_verification():
    from requests import Session

    session = Session()
    session.mount('https://', NoSSLVerificationAdapter())

    Session.request = session.request  # Переопределение метода 'request'
    yield  # После завершения тест сессии удалит себя


@pytest.fixture(scope="function")
def driver():
    # Настройки для WebDriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--no-sandbox')
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    if call.when == "call" and report.failed:
        driver = node.funcargs.get("driver")
        if driver:
            screenshot_folder = "screens"
            os.makedirs(screenshot_folder, exist_ok=True)
            screenshot_path = os.path.join(screenshot_folder, f"screenshot_{report.nodeid.replace('/', '_')}.png")
            driver.save_screenshot(screenshot_path)
            testit.addAttachments(screenshot_path)
            print(f"Скриншот сохранен: {screenshot_path}")
