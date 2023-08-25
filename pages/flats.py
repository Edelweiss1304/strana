from base.base_class import Base
from selenium.webdriver.common.by import By
import testit


class Flats(Base):
    # locators
    more_params = "//span[contains(text(),'Еще параметры')]"
    action_cb = "//input[@id='f80427bb-9280-2c69-c01d-a4b516e24b56']"

    # Getters
    def get_more_params(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.more_params))

    def get_checkbox_action(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.action_cb))

    # Actions

    def click_more_params(self):
        self.get_more_params().click()

    # Methods
    def assert_action_active(self):
        with testit.step("Нажимаем кнопку Еще параметры"):
            self.click_more_params()
            print(self.get_checkbox_action())
            # assert self.get_checkbox_action().get_attribute("checked") == "checked"
