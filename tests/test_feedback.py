from pages.feedback import FeedBack
from pages.header_links import Header
from base.base_class import Base
from pages.url import URLS_MAIN
import pytest
import time


@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_feedback_main_page(driver, url):
    fb = FeedBack(driver)
    Base.open_page(driver, url)
    fb.get_phone().send_keys(+9921275687)
    time.sleep(5)
    fb.get_name().send_keys("ТЕСТ")
    time.sleep(5)
    fb.get_submit().click()
    time.sleep(5)


@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_feedback_projects_page(driver, url):
    fb = FeedBack(driver)
    head = Header(driver)
    Base.open_page(driver, url)
    head.get_projects().click()
    fb.get_phone_projects().send_keys(+9921275687)
    time.sleep(5)
    fb.get_name_projects().send_keys("ТЕСТ")
    time.sleep(5)
    fb.get_submit_projects().click()
    time.sleep(5)


@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_feedback_actions_page(driver, url):
    fb = FeedBack(driver)
    head = Header(driver)
    Base.open_page(driver, url)
    head.get_action().click()
    time.sleep(5)
    driver.refresh()
    fb.get_phone_projects().send_keys(+9921275687)
    time.sleep(5)
    fb.get_name_projects().send_keys("ТЕСТ")
    time.sleep(5)
    fb.get_submit_projects().click()
    time.sleep(5)
