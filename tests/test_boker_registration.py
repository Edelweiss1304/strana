from pages.broker_registration import BrokerRegistration
from base.base_class import Base
from pages.url import URLS_MAIN
import pytest
import testit
import time
import os

url_broker = 'https://broker.strana.com/login'


@testit.displayName("Проверка регистрации в ЛК брокера для агента")
@testit.description("Проверка регистрации в ЛК брокера для агента")
@pytest.mark.parametrize("url", [url_broker])
def test_registration_agent(driver, url):
    reg = BrokerRegistration(driver)
    with testit.step("Открываем страницу входа"):
        Base.open_page(driver, url)
    with testit.step("Нажимаем на регистрацию"):
        reg.get_first_registration_button().click()
    with testit.step("Вводим ИНН"):
        reg.get_inn_for_agent().send_keys(1000000001)
    with testit.step("Нажимаем продолжить"):
        reg.get_continue_button_for_agent_1().click()
    with testit.step("Заолняем информацию об агенте"):
        reg.get_surname_registration_field().send_keys("Дмитриев")
        reg.get_name_rigistration_field().send_keys("Алексей")
        reg.get_second_name_rigistration_field().send_keys("Владимирович")
        reg.get_phone_rigistration_field().send_keys(9198629250)
        reg.get_email_rigistration_field().send_keys("smiledmitriev1@gmail.com")
        reg.get_password_rigistration_field().send_keys(1234567890)
        reg.get_second_password_rigistration_field().send_keys(1234567890)
        reg.get_fin_registration_button().click()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 10000);")
        time.sleep(5)
        reg.get_confirm_reglament_button().click()
        assert driver.current_url == "broker.strana.com/deals"
        time.sleep(10)


@testit.displayName("Проверка регистрации в ЛК брокера для агентства")
@testit.description("Проверка регистрации в ЛК брокера для агентства")
@pytest.mark.parametrize("url", [url_broker])
def test_registration_agency(driver, url):
    reg = BrokerRegistration(driver)
    with testit.step("Открываем страницу входа"):
        Base.open_page(driver, url)
    with testit.step("Нажимаем на регистрацию"):
        reg.get_first_registration_button().click()
    with testit.step("Меняем таб регистрации на агентсво"):
        reg.get_switch_agent_agency().click()
    with testit.step("Заполняем поля для регистрации"):
        reg.get_inn_for_agency().send_keys(5656565656)
        reg.get_name_agency().send_keys("Автотестовое агентство")
        reg.get_city_agency().send_keys("Тюмень")
        absolute_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'screens', 'testpdf.pdf'))
        reg.get_agency_doc_1().send_keys(absolute_file_path)
        reg.get_agency_doc_2().send_keys(absolute_file_path)
        time.sleep(5)
        reg.get_continue_button_for_agent_1().click()
    with testit.step("Заполняем поля ПД для директора"):
        reg.get_surname_registration_field().send_keys("Тестовый")
        reg.get_name_rigistration_field().send_keys("Директор")
        reg.get_second_name_rigistration_field().send_keys("Директорович")
        driver.execute_script("arguments[0].click();", reg.get_position_field_registration())
        reg.get_position_field_registration_director().click()
        reg.get_phone_rigistration_field().send_keys(9198629250)
        reg.get_email_rigistration_field().send_keys("anymail123123@mail.com")
        reg.get_password_rigistration_field().send_keys(1234567890)
        reg.get_second_password_rigistration_field().send_keys(1234567890)
        reg.get_fin_registration_button().click()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 10000);")
        time.sleep(5)
        reg.get_confirm_reglament_button().click()
        time.sleep(10)
