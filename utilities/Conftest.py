import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import os


# @pytest.fixture(scope="function")
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument("--headless")
#     caps = DesiredCapabilities().CHROME
#     caps["pageLoadStrategy"] = "eager"
#     driver = webdriver.Chrome(desired_capabilities=caps, options=options)
#     driver.set_window_size(1920, 1080)
#     yield driver
#     driver.quit()

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
        # Check if setup or call phase has failed.
        if hasattr(request.node, "rep_setup") and not request.node.rep_setup.passed:
            failed = True
        elif hasattr(request.node, "rep_call") and not request.node.rep_call.passed:
            failed = True
        else:
            failed = False

        if failed:
            if not os.path.exists("/home/strana_test/screens"):
                os.makedirs("/home/strana_test/screens")
            driver.save_screenshot(f"/home/strana_test/screens/FAILURE_{request.node.name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
        driver.quit()

    request.addfinalizer(fin)
    return driver
