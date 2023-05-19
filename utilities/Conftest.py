import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime


@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--headless")
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Chrome(desired_capabilities=caps, options=options)
    driver.set_window_size(1920, 1080)

    def fin():
        if request.node.rep_setup.failed:
            driver.get_screenshot_as_file(
                'screens/{}_{}.png'.format(driver.current_url.replace('/', '_'), datetime.now().isoformat()))
        driver.quit()

    request.addfinalizer(fin)
    return driver
