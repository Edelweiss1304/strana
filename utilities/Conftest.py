import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="module")
def driver():
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    sauce_options = {}
    caps['sauce:options']['build'] = 'Edelweiss1304'
    caps['sauce:options']['name'] = 'Strana'
    options.set_capability('sauce:options', sauce_options)
    driver = webdriver.Chrome(desired_capabilities=caps, options=options)
    yield driver
    driver.quit()
