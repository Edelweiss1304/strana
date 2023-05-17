import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:  # if the test has failed
        # Save a screenshot with the test name and date-time
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        item.instance.driver.save_screenshot(f"{item.nodeid}_{timestamp}.png")
