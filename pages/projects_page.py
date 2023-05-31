from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProjectsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Локаторы
    wow = "//a[@href='/projects/business/wow/']"
    ozerniy = "//a[@href='/projects/business/stranaozernaya/']"
    dnv = "(//a[@class='project-card ProjectCard_zxjuT _vice_fQOtu _light_blue_LHxX7'])[1]"
    princip = "(//a[@class='project-card ProjectCard_zxjuT _vice_fQOtu _aquamarine_80wfM'])[1]"
    sibsad = "(//a[@class='project-card ProjectCard_zxjuT _vice_fQOtu _light_blue_LHxX7'])[1]"
    zvezdniy = "(//a[@class='project-card ProjectCard_zxjuT _moxxy_1ai6F _aquamarine_80wfM'])[1]"
    union = "(//a[@class='project-card ProjectCard_zxjuT _vice_fQOtu _light_blue_LHxX7'])[1]"
    avtorskiy = "(//a[@class='project-card ProjectCard_zxjuT _vice_fQOtu _light_blue_LHxX7'])[2]"
    kolumb = "//a[@class='project-card ProjectCard_zxjuT _elysium_bWqag _dark_blue_CRQPA']"
    sersib = "(//a[@class='project-card ProjectCard_zxjuT _vice_fQOtu _light_blue_LHxX7'])[3]"
    domashniy = "(//a[@class='project-card ProjectCard_zxjuT _vice_fQOtu _light_blue_LHxX7'])[4]"

    # Геттеры
    def get_wow(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.wow))

    def get_ozerniy(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.ozerniy))

    def get_dnv(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.dnv))

    def get_princip(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.princip))

    def get_sibsad(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.sibsad))

    def get_zvezdniy(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.zvezdniy))

    def get_union(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.union))

    def get_avtorskiy(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.avtorskiy))

    def get_kolumb(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.kolumb))

    def get_sersib(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.sersib))

    def get_domashniy(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.domashniy))

    # Actions

    def click_wow(self):
        self.get_wow().click()

    def click_ozerniy(self):
        self.get_ozerniy().click()

    def click_dnv(self):
        self.get_dnv().click()

    def click_princip(self):
        self.get_princip().click()

    def click_sibsad(self):
        self.get_sibsad().click()

    def click_zvezdniy(self):
        self.get_zvezdniy().click()

    def click_union(self):
        self.get_union().click()

    def click_avtorskiy(self):
        self.get_avtorskiy().click()

    def click_kolumb(self):
        self.get_kolumb().click()

    def click_sersib(self):
        self.get_sersib().click()

    def click_domashniy(self):
        self.get_domashniy().click()