import requests
from utilities.Conftest import driver


class Base:
    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def open_page(cls, driver, url):
        driver.get(url)

    @classmethod
    def check_url_end(cls, driver, end):
        current_url = driver.current_url
        if current_url.endswith(end):
            return True
        else:
            return False

    @classmethod
    def check_page_status(cls, driver):
        url = driver.current_url
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False

    # URL
    url_tmn = 'https://tmn.strana.com'
    url_msk = 'https://msk.strana.com'
    url_spb = 'https://spb.strana.com'
    url_mo = 'https://mo.strana.com'
    url_ekb = 'https://ekb.strana.com'
    url_nsk = 'https://nsk.strana.com'
