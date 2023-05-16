from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Header(Base):
    # Locators

    projects = "//span[@class='s-shift-text__value'][contains(text(),'Проекты')]"
    apart = "//span[@class='s-shift-text__value'][contains(text(),'Квартиры')]"
    commercial = "//span[@class='s-shift-text__value'][contains(text(),'Коммерция')]"
    action = "//span[@class='s-shift-text__value'][contains(text(),'Акции')]"
    about = "//span[@class='s-shift-text__value'][contains(text(),'О компании')]"
    purchase_methods = "//span[@class='s-shift-text__value'][contains(text(),'Способы покупки')]"
    vacancies = "//span[@class='s-shift-text__value'][contains(text(),'Вакансии')]"
    menu = "//span[@class='s-shift-text__value'][contains(text(),'Меню')]"

    purchase_methods_check = "//h1[contains(text(),'Способы покупки')]"
    projects_check = "//h1[contains(text(),'Проекты')]"
    apart_check = "//div[@class='s-select__label' and text()='Подобрать квартиру']"
    action_check = "(//span[contains(text(),'Акции')])[3]"
    about_check = "//h1[contains(text(),'О компании')]"
    vacancy_check = "//h1[contains(text(),'Работа в Стране Девелопмент')]"

    # Getters
    def get_projects(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.projects)))

    def get_apart(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.apart)))

    def get_commercial(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.commercial)))

    def get_action(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.action)))

    def get_about(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.about)))

    def get_purchase_methods(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.purchase_methods)))

    def get_vacancies(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.vacancies)))

    def get_menu(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.menu)))

    def get_purchase_methods_check(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.purchase_methods_check))).text

    def get_apart_check(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.apart_check))).text

    def get_projects_check(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.projects_check))).text

    def get_actions_check(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.action_check))).text

    def get_about_check(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.about_check))).text

    def get_vacancy_check(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.vacancy_check))).text
    # Actions

    def click_projects(self):
        self.get_projects().click()

    def click_apart(self):
        self.get_apart().click()

    def click_commercial(self):
        self.get_commercial().click()

    def click_action(self):
        self.get_action().click()

    def click_about(self):
        self.get_about().click()

    def click_purchase_methods(self):
        self.get_purchase_methods().click()

    def click_vacancies(self):
        self.get_vacancies().click()

    # Methods
    def check_projects(self):
        self.click_projects()
        assert Base.check_page_status(self.driver) == True
        assert self.get_projects_check() == "Проекты"

    def check_apart(self):
        self.click_apart()
        assert Base.check_page_status(self.driver) == True
        assert self.get_apart_check() == "Подобрать квартиру"

    def check_commercial(self):
        self.click_commercial()
        assert Base.check_page_status(self.driver) == True
        assert self.get_projects_check() == "Проекты"

    def check_actions(self):
        self.click_action()
        assert Base.check_page_status(self.driver) == True
        assert self.get_actions_check() == "Акции"

    def check_about(self):
        self.click_about()
        assert Base.check_page_status(self.driver) == True
        assert self.get_about_check() == "О компании"

    def check_purchase_methods(self):
        self.click_purchase_methods()
        assert Base.check_page_status(self.driver) == True
        assert self.get_purchase_methods_check() == "Способы покупки"

    def check_vacancies(self):
        self.click_vacancies()
        assert Base.check_page_status(self.driver) == True
        assert self.get_about_check() == "О компании"
        assert self.get_vacancy_check() == "Работа в Стране Девелопмент"
