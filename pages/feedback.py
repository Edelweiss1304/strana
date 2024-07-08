from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class FeedBack(Base):
    # ЛОКАТОРЫ
    mane = "//input[@placeholder='Имя']"
    phone = "//input[@placeholder='Телефон']"
    submit = "//span[contains(text(),'Оставить заявку')]"
    phone_projects = "//input[@type='tel']"
    name_projects = "//input[@type='text']"
    submit_projects = "//button[@type='submit']"

    purchase_button = "//a[contains(@class, 'the-header-base__label') and contains(@class, 's-tag--primary-common')]"
    request_button = "//button[@class='s-button s-mortgage-filter__btn s-button--default s-button--primary s-button--design-common s-button--rounded' and .//span[contains(text(), 'Оставить заявку')]]"
    input_name = "//input[@placeholder='Имя и фамилия']"
    input_tel = "//input[@placeholder='Номер телефона']"
    request_call_button = "//button[.//span[contains(text(), 'Заказать звонок')]]"
    # GETTERS
    def get_name(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.mane))

    def get_phone(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.phone))

    def get_submit(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.submit))

    def get_name_projects(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.name_projects))

    def get_phone_projects(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.phone_projects))

    def get_submit_projects(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.submit_projects))

    def get_purchase_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.purchase_button))

    def get_request_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.request_button))

    def get_input_name(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.input_name))

    def get_input_tel(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.input_tel))

    def get_request_call_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.request_call_button))
