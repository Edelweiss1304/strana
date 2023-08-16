from base.base_class import Base
from selenium.webdriver.common.by import By
from pages.url import URLS_MAIN
import pytest
import time
from pages.header_links import Header
import testit


class Authorization(Base):
    # Locators
    login_lk_button = "//span[@class='the-header__icons-item']"
    login_client_phone_field = "//input[@type ='tel']"
    get_code_btn = "//span[@class='v-btn__content']"
    enter_code_field = "//input[@type ='number']"
    fin_login_btn = "//span[contains(text(),'Войти')]"
    check_lk = "//h1[contains(text(),'Брони и договоры')]"

    first_login_broker_button = "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[1]/div[2]/a[2]"
    email_field_agent = "email"
    password_field_agent = "//label[text()='Пароль']/following-sibling::input"
    login_broker_btn = "//button[@type='submit']"
    broker_agent_check = "//h1[contains(text(),'Сделки')]"

    # Getters

    def get_login_lk_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.login_lk_button))

    def get_login_client_phone_field(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.login_client_phone_field))

    def get_enter_code_field(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.enter_code_field))

    def get_get_code_btn(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.get_code_btn))

    def get_fin_login_btn(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.fin_login_btn))

    def get_check_lk(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.check_lk)).text

    def get_email_field_agent(self):
        return self.get_element_clickable(self.driver, (By.NAME, self.email_field_agent))

    def get_password_field_agent(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.password_field_agent))

    def get_login_broker_btn(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.login_broker_btn))

    def get_broker_agent_check(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.broker_agent_check))

    def get_first_login_broker_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.first_login_broker_button))

    # Actions

    def click_login_lk_button(self):
        self.get_login_lk_button().click()
        print('Нажата кнопка входа в аккаунт в хэдере')

    def click_get_code_btn(self):
        self.get_get_code_btn().click()
        print('Нажата кнопка получить код')

    def click_fin_login_btn(self):
        self.get_fin_login_btn().click()
        print('Нажата финальная кнопка входа в аккаунт')

    def click_login_broker_btn(self):
        self.get_login_broker_btn().click()
        print('Нажата кнопка входа для брокера')

    def click_first_login_broker_button(self):
        self.get_first_login_broker_button().click()
        print('Нажата кнопка входа для брокера на посадочной странице')

    # Methods
    def login_lk(self, phone_for_user=+79198629250, code_for_user=1313):
        time.sleep(1)
        with testit.step("Нажимаем иконку входа"):
            self.click_login_lk_button()
            next_tab_index = (self.driver.window_handles.index(self.driver.current_window_handle) + 1) % len(self.driver.window_handles)
        with testit.step("Переключаемся на соседнюю вкладку"):
            self.driver.switch_to.window(self.driver.window_handles[next_tab_index])
        with testit.step("Заполняем телефон"):
            self.get_login_client_phone_field().send_keys(phone_for_user)
        with testit.step("Кликаем Получить код"):
            self.click_get_code_btn()
        with testit.step("Вводим код"):
            self.get_enter_code_field().send_keys(code_for_user)
        with testit.step("Нажимаем Войти"):
            self.click_fin_login_btn()

    def login_page_broker_from_header(self, url):
        head = Header(self.driver)
        time.sleep(1)
        with testit.step("Открываем главную страницу"):
            head.actions.move_to_element(head.get_menu_button()).perform()

            if url == 'https://mo.strana.com':
                locator = Base.get_s_link_wrapper_locator(23)

            elif url == 'https://nsk.strana.com':
                locator = Base.get_s_link_wrapper_locator(20)

            elif url == 'https://msk.strana.com':
                locator = Base.get_s_link_wrapper_locator(24)

            else:
                locator = Base.get_s_link_wrapper_locator(25)
        with testit.step("Кликаем на Агентам и агентствам"):
            Base.get_element_visibility(self.driver, (By.XPATH, locator)).click()
        with testit.step("Нажимаем Войти/Зарегистрироваться"):
            self.click_first_login_broker_button()

    def login_lk_broker(self, email='smiledmitriev@yandex.com', password='123456789'):
        with testit.step("Вводим почту"):
            time.sleep(2)
            self.get_email_field_agent().send_keys(email)
        with testit.step("Вводим пароль"):
            self.get_password_field_agent().send_keys(password)
        with testit.step("Нажимаем Войти"):
            self.click_login_broker_btn()

    def login_broker_from_main_page(self, url):
        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(12)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(8)

        elif url == 'https://spb.strana.com':
            locator = Base.get_s_link_wrapper_locator(17)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(15)

        elif url == 'https://ekb.strana.com':
            locator = Base.get_s_link_wrapper_locator(20)

        else:
            locator = Base.get_s_link_wrapper_locator(19)
        with testit.step("Кликаем Агентам и агентствам на главном экране"):
            Base.get_element_visibility(self.driver, (By.XPATH, locator)).click()
        with testit.step("Нажимаем Войти"):
            self.click_first_login_broker_button()
