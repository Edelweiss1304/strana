import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="function")
def driver(request):
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

    def fin():
        if request.node.rep_call.failed:
            driver.get_screenshot_as_file(
                'screens/{}_{}.png'.format(driver.current_url.replace('/', '_'), datetime.now().isoformat()))
        driver.quit()

    request.addfinalizer(fin)
    return driver
