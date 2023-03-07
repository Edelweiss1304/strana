from pages.main_page_tmn import MainPageTmn
from utilities.Conftest import driver
import time


def test_authorization_tmn(driver):
    mpt = MainPageTmn(driver)
    mpt.open_main_tmn()
    mpt.authorization()
    time.sleep(5)
