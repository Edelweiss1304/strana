from base.base_class import Base
from selenium.webdriver.common.by import By
import testit


class CityChange(Base):
    # Locators
    city_select_header = "//div[@class='s-tooltip-wrapper the-header-city-tooltip']"
    city_header_msk = "// li[contains(text(), 'Москва')]"
    city_header_mo = "// li[contains(text(), 'Московская область')]"
    city_header_spb = "// li[contains(text(), 'Санкт-Петербург')]"
    city_header_ekb = "// li[contains(text(), 'Екатеринбург')]"
    city_header_tmn = "// li[contains(text(), 'Тюмень')]"
    city_header_nsk = "// li[contains(text(), 'Новосибирск')]"

    # Getters
    def get_city_select_header(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.city_select_header))

    def get_city_header_mo(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.city_header_mo))

    def get_city_header_msk(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.city_header_msk))

    def get_city_header_spb(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.city_header_spb))

    def get_city_header_ekb(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.city_header_ekb))

    def get_city_header_tmn(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.city_header_tmn))

    def get_city_header_nsk(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.city_header_nsk))