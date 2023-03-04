from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPageTmn(Base):
    url = 'https://tmn.strana.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    """Кнопка авторизации в ЛК"""
    login_lk_button = "//button[@class='btn-reset btn_FPa8J accountBtn_du0F7']"

    # Getters

    def get_login_lk_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_lk_button)))

    # Actions

    def click_login_lk_button(self):
        self.get_login_lk_button().click()
        print('Нажата кнопка входа в аккаунт')

    # Methods
    def open_main_tmn(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def authorization(self):
        self.click_login_lk_button()
