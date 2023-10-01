from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProjectsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Локаторы
    wow = "//h2[contains(text(),'ЖК WOW')]"
    ozerniy = "//h2[contains(text(),'Страна.Озерная')]"
    dnv = "//h2[contains(text(),'Дом на Васильевском')]"
    princip = "//h2[contains(text(),'ПРИНЦИП')]"
    sibsad = "//h2[contains(text(),'Сибирский сад')]"
    zvezdniy = "//h2[contains(text(),'Звездный')]"
    union = "//h2[contains(text(),'Юнион')]"
    avtorskiy = "//h2[contains(text(),'Авторский')]"
    kolumb = "//h2[contains(text(),'Колумб')]"
    sersib = "//h2[contains(text(),'Сердце Сибири')]"
    domashniy = "//h2[contains(text(),'Домашний')]"
    eb = "//h2[contains(text(),'Европейский берег 2.0')]"

    accept_cookie = "//span[contains(text(),'Принять')]"

    # Локаторы для кнопок квартир
    wow_flats_button = "//h3[text()='ЖК WOW']/following::button[contains(@class,'btn_WWmef')]"
    ozernya_flats_button = "//h3[text()='Страна.Озерная']/following::button[contains(@class,'btn_WWmef')]"
    sibsad_flats_button = "//h3[text()='Сибирский сад']/following::button[contains(@class,'btn_WWmef')]"
    zvezdniy_flats_button = "//h3[text()='Звездный']/following::button[contains(@class,'btn_WWmef')]"
    union_flats_button = "//h3[text()='Юнион']/following::button[contains(@class,'btn_WWmef')]"
    avtorskiy_flats_button = "//h3[text()='Авторский']/following::button[contains(@class,'btn_WWmef')]"
    sersib_flats_button = "//h3[text()='Сердце Сибири']/following::button[contains(@class,'btn_WWmef')]"
    domashniy_flats_button = "//h3[text()='Домашний']/following::button[contains(@class,'btn_WWmef')]"
    eb2_flats_button = "//h3[text()='Европейский берег 2.0']/following::button[contains(@class,'btn_WWmef')]"

    # Геттеры
    def get_wow(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.wow))

    def get_ozerniy(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.ozerniy))

    def get_dnv(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.dnv))

    def get_princip(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.princip))

    def get_sibsad(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.sibsad))

    def get_zvezdniy(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.zvezdniy))

    def get_union(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.union))

    def get_avtorskiy(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.avtorskiy))

    def get_kolumb(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.kolumb))

    def get_sersib(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.sersib))

    def get_domashniy(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.domashniy))

    def get_eb(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.eb))

    def get_accept_cookie(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.accept_cookie))

    def get_wow_flats_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.wow_flats_button))

    def get_ozernya_flats_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.ozernya_flats_button))

    def get_sibsad_flats_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.sibsad_flats_button))

    def get_zvezdniy_flats_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.zvezdniy_flats_button))

    def get_union_flats_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.union_flats_button))

    def get_avtorskiy_flats_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.avtorskiy_flats_button))

    def get_sersib_flats_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.sersib_flats_button))

    def get_domashniy_flats_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.domashniy_flats_button))

    def get_eb2_flats_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.eb2_flats_button))


