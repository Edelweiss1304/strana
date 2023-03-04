import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="module")
def driver():
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    sauce_options = {'build': 'Edelweiss1304', 'name': 'Strana'}
    options.set_capability('sauce:options', sauce_options)
    caps = DesiredCapabilities.CHROME.copy()
    caps['platform'] = 'Windows 11'
    caps['version'] = 'latest'
    url = "https://oauth-smiledmitriev-8567c:*****73fe@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    driver = webdriver.Remote(
        command_executor=url, desired_capabilities=caps, options=options
    )
    yield driver
    driver.quit()