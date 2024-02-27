from base.base_class import Base
from selenium.webdriver.common.by import By


class Lk(Base):
    # Locators
    uniqueness_button = "//div[contains(text(), 'Проверить клиента на уникальность')]"
    uniqueness_input = "//label[text()='Номер телефона']/../input"
    uniqueness_button_popup = "//span[contains(text(), 'Проверить')]"
    result_uniqueness = "//div[contains(text(), 'Уникальный')]"

    # Getter's
    def get_uniqueness_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_button))

    def get_uniqueness_input(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_input))

    def get_uniqueness_button_popup(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_button_popup))

    def get_result_uniqueness(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.result_uniqueness))
