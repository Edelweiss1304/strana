from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import testit


class ProjectsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Локаторы
    wow = "//a[@href='/projects/business/wow/']"
    ozerniy = "//a[@href='/projects/business/stranaozernaya/']"
    dnv = "//h3[contains(text(),'Дом на Васильевском')]"
    princip = "//h3[contains(text(),'ПРИНЦИП')]"
    sibsad = "//h3[contains(text(),'Сибирский сад')]"
    zvezdniy = "//h3[contains(text(),'Звездный')]"
    union = "//h3[contains(text(),'Юнион')]"
    avtorskiy = "//h3[contains(text(),'Авторский')]"
    kolumb = "//h3[contains(text(),'Колумб')]"
    sersib = "//h3[contains(text(),'Сердце Сибири')]"
    domashniy = "//h3[contains(text(),'Домашний')]"
    eb = "//h3[contains(text(),'Европейский берег 2.0')]"

    accept_cookie = "//span[contains(text(),'Принять')]"

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

    # Actions
    with testit.step("Кликаем на WOW"):
        def click_wow(self):
            self.get_wow().click()

    with testit.step("Кликаем на Озерный"):
        def click_ozerniy(self):
            self.get_ozerniy().click()

    with testit.step("Кликаем на ДнВ"):
        def click_dnv(self):
            self.get_dnv().click()

    with testit.step("Кликаем на Озерный"):
        def click_princip(self):
            self.get_princip().click()

    with testit.step("Кликаем на Сибирский Сад"):
        def click_sibsad(self):
            self.get_sibsad().click()

    with testit.step("Кликаем на Звездный"):
        def click_zvezdniy(self):
            self.get_zvezdniy().click()

    with testit.step("Кликаем на Юнион"):
        def click_union(self):
            self.get_union().click()

    with testit.step("Кликаем на Авторский"):
        def click_avtorskiy(self):
            self.get_avtorskiy().click()

    with testit.step("Кликаем на Колумб"):
        def click_kolumb(self):
            self.get_kolumb().click()

    with testit.step("Кликаем на Сердце Сибири"):
        def click_sersib(self):
            self.get_sersib().click()

    with testit.step("Кликаем на Домашний"):
        def click_domashniy(self):
            self.get_domashniy().click()

    with testit.step("Принимаем куки"):
        def click_accept_cookie(self):
            self.get_accept_cookie().click()

    with testit.step("Кликаем на ЕБ 2.0"):
        def click_eb(self):
            self.get_eb().click()
