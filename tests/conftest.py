import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from requests.sessions import Session
import os
import testit
from requests.adapters import HTTPAdapter
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning


class NoSSLVerificationAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        kwargs['cert_reqs'] = 'CERT_NONE'
        super(NoSSLVerificationAdapter, self).init_poolmanager(*args, **kwargs)


# Фикстура для отключения SSL верификации
@pytest.fixture(scope='session', autouse=True)
def no_ssl_verification():
    disable_warnings(InsecureRequestWarning)
    session = Session()
    adapter = NoSSLVerificationAdapter()
    session.mount('https://', adapter)
    old_request = Session.request
    def new_request(*args, **kwargs):
        kwargs['verify'] = False
        return old_request(*args, **kwargs)
    Session.request = new_request
    yield  # Возвращаем контроль в конце тестовой сессии


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
    options.add_argument('--headless')  # Добавить для запуска без графического интерфейса, если нужно
    service = Service(executable_path='./chromedriver')  # Указать путь к chromedriver, если необходимо
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
            screenshot_path = os.path.join(screenshot_folder, report.nodeid.replace('::', '_') + ".png")
            driver.save_screenshot(screenshot_path)
            testit.addAttachments(screenshot_path)
            print(f"Скриншот сохранен: {screenshot_path}")


# Удалите или закомментируйте фикстуру disable_ssl_verification, так как она больше не нужна
# @pytest.fixture(autouse=True)
# def disable_ssl_verification(requests_mock):
#     requests_mock.get('https://172.16.251.133/api/v2/testRuns', text='mocked response', verify=False)
