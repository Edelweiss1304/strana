import pytest
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import testit
from pages.flats import Flats


class ProjectsFromHeader(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.Base = Base
        self.driver = driver
        self.actions = ActionChains(driver)

    # Локаторы для проектов в выпадающем меню
    wow = "//li[@class='header-projects-popup__project' and .//p[contains(text(),'ЖК WOW')]]"
    ozernaya = "//li[@class='header-projects-popup__project' and .//p[contains(text(),'Страна.Озерная')]]"
    dnv = "//li[@class='header-projects-popup__project' and .//p[contains(text(),'Дом на Васильевском')]]"
    sibsad = "//li[@class='header-projects-popup__project' and .//p[contains(text(),'Сибирский сад')]]"
    zvezdniy = "//li[@class='header-projects-popup__project' and .//p[contains(text(),'Звездный')]]"
    union = "//li[@class='header-projects-popup__project' and .//p[contains(text(),'Юнион')]]"
    avtorskiy = "//li[@class='header-projects-popup__project' and .//p[contains(text(),'Авторский')]]"
    eb2 = "//li[@class='header-projects-popup__project' and .//p[contains(text(),'Европейский берег 2.0')]]"
    sersib = "//li[@class='header-projects-popup__project' and .//p[contains(text(),'Сердце Сибири')]]"
    domashniy = "//li[@class='header-projects-popup__project' and .//p[contains(text(),'Домашний')]]"

    project_business_tittle = "//div[@class='uppercase title_KrDfI']"
    project_comfort_tittle = ".project-hero__title"
    dnv_tittle = "(//div[@class='listLabel_Q6E55'][contains(text(),'Санкт-Петербург')])"

    projects = "//span[@class='s-shift-text__value'][contains(text(),'Проекты')]"

    # Getters
    def get_wow(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.wow))

    def get_ozernaya(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.ozernaya))

    def get_dnv(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.dnv))

    def get_sibsad(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.sibsad))

    def get_zvezdiy(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.zvezdniy))

    def get_union(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.union))

    def get_avtorskiy(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.avtorskiy))

    def get_eb2(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.eb2))

    def get_sersib(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.sersib))

    def get_domashniy(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.domashniy))

    def get_project_business_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.project_business_tittle)).text

    def get_project_comfort_tittle(self):
        return self.get_element_visibility(self.driver, (By.CSS_SELECTOR, self.project_comfort_tittle)).text

    def get_projects_button(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.projects))

    def get_dnv_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.dnv_tittle)).text
