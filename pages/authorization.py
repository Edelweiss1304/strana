from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Authorization(Base):

    # Locators
    login_lk_button = "//button[@id='link-account']"
    continue_lk_btn = "(//button[@class='v-button v-button--default v-button--medium is-rounded _position_SEIu5'])[1]"
    login_client_phone_field = "//input[@type='tel']"
    get_code_btn = "button[value='false'][type='submit']"
    enter_code_field = "//input[@required='required']"
    fin_login_btn = "(//button[@id='Pty6zL2WDf5KpaNB2Teja'])[1]"
    check_lk = "//h1[contains(text(),'Брони и договоры')]"
    switch_btn_partner = "(//div[@class='link_ARf12'])[1]"
    switch_btn_agency = "//div[contains(text(), 'Агентство')]"
    email_field_agent = "email"
    password_field_agent = "//label[contains(text(), 'Пароль')]/following-sibling::input[@type='password']"
    email_field_agency = "email"
    password_field_agency = "//label[contains(text(), 'Пароль')]/following-sibling::input[@type='password']"
    login_broker_btn = "//span[contains(text(),'Войти')]"
    broker_agent_check = '//h1[contains(text(),"Клиенты")]'

    # Getters

    def get_login_lk_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.login_lk_button)))

    def get_continue_lk_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_lk_btn)))

    def get_login_client_phone_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_client_phone_field)))

    def get_enter_code_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_code_field)))

    def get_get_code_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.get_code_btn)))

    def get_fin_login_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fin_login_btn)))

    def get_check_lk(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.check_lk))).text

    def get_switch_btn_agency(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.switch_btn_agency)))

    def get_switch_btn_partner(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.switch_btn_partner)))

    def get_email_field_agent(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, self.email_field_agent)))

    def get_password_field_agent(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.password_field_agent)))

    def get_email_field_agency(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, self.email_field_agency)))

    def get_password_field_agency(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.password_field_agency)))

    def get_login_broker_btn(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_broker_btn)))

    def get_broker_agent_check(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.broker_agent_check)))

    # Actions

    def click_login_lk_button(self):
        self.get_login_lk_button().click()
        print('Нажата кнопка входа в аккаунт в хэдэре')

    def click_continue_btn(self):
        self.get_continue_lk_btn().click()
        print('Нажата кнопка продолжить')

    def click_get_code_btn(self):
        self.get_get_code_btn().click()
        print('Нажата кнопка получить код')

    def click_fin_login_btn(self):
        self.get_fin_login_btn().click()
        print('Нажата финальная кнопка входа в аккаунт')

    def check_lk_authorization(self):
        assert self.get_check_lk() == "Брони и договоры"
        print('Успешный вход в ЛК')

    def click_switch_btn_partner(self):
        self.get_switch_btn_partner().click()
        print('Нажата кнопка партнер')

    def click_login_broker_btn(self):
        self.get_login_broker_btn().click()
        print('Нажата кнопка входа для брокера')

    def check_broker_agent(self):
        assert self.get_broker_agent_check().text == "Клиенты"
        print('Успешный вход в ЛК брокера')

    def click_switch_btn_agency(self):
        self.get_switch_btn_agency().click()
        print('Переключаемся на агентство')

    # Methods

    def login_lk(self, phone_for_user=+79198629250, code_for_user=1313):
        self.click_login_lk_button()
        self.click_continue_btn()
        self.get_login_client_phone_field().send_keys(phone_for_user)
        self.click_get_code_btn()
        self.get_enter_code_field().send_keys(code_for_user)
        self.click_fin_login_btn()

    def login_lk_broker_agent(self, email='smiledmitriev@yandex.com', password='123456789'):
        self.click_login_lk_button()
        self.click_switch_btn_partner()
        self.click_continue_btn()
        self.get_email_field_agent().send_keys(email)
        self.get_password_field_agent().send_keys(password)
        self.click_login_broker_btn()

    def login_lk_broker_agency(self, email='dmitrievaleks777@rambler.ru', password='1234567890'):
        self.click_login_lk_button()
        self.click_switch_btn_partner()
        self.click_continue_btn()
        self.click_switch_btn_agency()
        self.get_email_field_agency().send_keys(email)
        self.get_password_field_agency().send_keys(password)
        self.click_login_broker_btn()
