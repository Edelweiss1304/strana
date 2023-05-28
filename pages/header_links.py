from base.base_class import Base
from selenium.webdriver.common.by import By
import allure
import pytest


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

    purchase_methods_check = "//h1[contains(text(),'Материнский')]"
    projects_check = "//h2[contains(text(),'Проекты')]"
    apart_check = "//div[@class='s-select__label' and text()='Подобрать квартиру']"
    action_check = "(//span[contains(text(),'Акции')])[3]"
    about_check = "//h1[contains(text(),'О компании')]"
    vacancy_check = "//h2[contains(text(),'Работа в Стране Девелопмент')]"

    # Getters
    def get_projects(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.projects))

    def get_apart(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.apart))

    def get_commercial(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.commercial))

    def get_action(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.action))

    def get_about(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.about))

    def get_purchase_methods(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.purchase_methods))

    def get_vacancies(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.vacancies))

    def get_menu(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.menu))

    def get_purchase_methods_check(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.purchase_methods_check)).text

    def get_apart_check(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.apart_check)).text

    def get_projects_check(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.projects_check)).text

    def get_actions_check(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.action_check)).text

    def get_about_check(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.about_check)).text

    def get_vacancy_check(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.vacancy_check)).text

    # Actions
    def click_projects(self):
        self.get_projects().click()

    print("Кликаем на кнопку проекты")

    def click_apart(self):
        self.get_apart().click()
        print("Кликаем на кнопку квартиры")

    def click_commercial(self):
        self.get_commercial().click()
        print("Кликаем на кнопку коммерция")

    def click_action(self):
        self.get_action().click()
        print("Кликаем на кнопку акции")

    def click_about(self):
        self.get_about().click()
        print("Кликаем на кнопку о нас")

    def click_purchase_methods(self):
        self.get_purchase_methods().click()
        print("Кликаем на кнопку проекты")

    def click_vacancies(self):
        self.get_vacancies().click()
        print("Кликаем на кнопку вакансии")

        # Methods

    def check_projects(self):
        self.click_projects()
        assert self.get_projects_check() == "Проекты"
        print("Проверяем заголовок")

    def check_apart(self):
        self.click_apart()
        assert self.get_apart_check() == "Подобрать квартиру"
        print("Проверяем заголовок")

    def check_commercial(self):
        self.click_commercial()
        assert self.get_projects_check() == "Проекты"
        print("Проверяем заголовок")

    def check_actions(self):
        self.click_action()
        assert self.get_actions_check() == "Акции"
        print("Проверяем заголовок")

    def check_about(self):
        self.click_about()
        assert self.get_about_check() == "О компании"
        print("Проверяем заголовок")

    def check_purchase_methods(self):
        self.click_purchase_methods()
        assert self.get_purchase_methods_check() == "Материнский капитал"
        print("Проверяем заголовок")

    def check_vacancies(self):
        self.click_vacancies()
        assert self.get_about_check() == "О компании"
        assert self.get_vacancy_check() == "Работа в Стране Девелопмент"
        print("Проверяем заголовок")
