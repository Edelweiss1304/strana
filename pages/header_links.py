import time

import pytest

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Header(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Локаторы для кнопок в хэдере

    projects = "//span[@class='s-shift-text__value'][contains(text(),'Проекты')]"
    apart = "//span[@class='s-shift-text__value'][contains(text(),'Квартиры')]"
    commercial = "//span[@class='s-shift-text__value'][contains(text(),'Коммерция')]"
    action = "//span[@class='s-shift-text__value'][contains(text(),'Акции')]"
    about = "//span[@class='s-shift-text__value'][contains(text(),'О компании')]"
    purchase_methods = "//span[@class='s-shift-text__value'][contains(text(),'Способы покупки')]"
    vacancies = "//span[@class='s-shift-text__value'][contains(text(),'Вакансии')]"
    menu = "//span[@class='s-shift-text__value'][contains(text(),'Меню')]"

    # Заголовки для проверок из страниц хэдера

    purchase_methods_check = "//h1[contains(text(),'Материнский')]"
    projects_check = "//h2[contains(text(),'Проекты')]"
    apart_check = "//div[@class='s-select__label' and text()='Подобрать квартиру']"
    action_check = "(//span[contains(text(),'Акции')])[3]"
    about_check = "//h1[contains(text(),'О компании')]"
    vacancy_check = "//h2[contains(text(),'Работа в Стране Девелопмент')]"

    # Локаторы для подменю в хэдере

    project_business_tittle = "//div[@class='uppercase title_KrDfI']"
    project_comfort_tittle = ".title_S5gJM"
    project_dnv_check = "(//div[@class='listLabel_Q6E55'][contains(text(),'Санкт-Петербург')])[1]"
    city_in_apart = "div[class='s-select s-select--string s-select--secondary s-select--large'] div[" \
                    "class='s-select__rendered']"
    s_link_wrapper_9 = "(//div[@class='s-link__wrapper'])[9]"  # Первый элемент в основном меню
    s_link_wrapper_10 = "(//div[@class='s-link__wrapper'])[10]"  # Второй элемент в основном меню
    s_link_wrapper_11 = "(//div[@class='s-link__wrapper'])[11]"  # Третий элемент в основном меню
    s_link_wrapper_12 = "(//div[@class='s-link__wrapper'])[12]"  # Четвертый элемент в основном меню + паркинг в спб (почему-то)
    s_link_wrapper_13 = "(//div[@class='s-link__wrapper'])[13]"  # Пятый элемент в основном меню
    s_link_wrapper_14 = "(//div[@class='s-link__wrapper'])[14]"  # Шестой элемент в основном меню
    s_link_parking = "//a[@href='/parking']"  # Паркинг

    text_color = "rgba(146, 39, 143, 1)"
    apart_0 = "//span[contains(text(),'Студия')]"
    apart_1 = "//span[normalize-space()='1']"
    apart_2 = "//span[normalize-space()='2']"
    apart_3 = "//span[normalize-space()='3']"
    apart_4 = "//span[normalize-space()='4+']"
    parking_tittle = "(//h1[@class='title_gewxY h3 text-base-500'][contains(text(),'Паркинг')])[1]"

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

    # Проверка подменю в ХЭДЕРЕ Getters

    def get_project_business_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.project_business_tittle)).text

    def get_project_comfort_tittle(self):
        return self.get_element_visibility(self.driver, (By.CSS_SELECTOR, self.project_comfort_tittle)).text

    def get_project_dnv_check(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.project_dnv_check)).text

    def get_s_link_wrapper_9_header(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.s_link_wrapper_9))

    def get_s_link_wrapper_10_header(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.s_link_wrapper_10))

    def get_s_link_wrapper_11_header(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.s_link_wrapper_11))

    def get_s_link_wrapper_12_header(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.s_link_wrapper_12))

    def get_s_link_wrapper_13_header(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.s_link_wrapper_13))

    def get_s_link_wrapper_14_header(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.s_link_wrapper_14))

    def get_city_in_apart(self):
        return self.get_element_visibility(self.driver, (By.CSS_SELECTOR, self.city_in_apart)).text

    def get_apart_0(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.apart_0))

    def get_apart_1(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.apart_1))

    def get_apart_2(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.apart_2))

    def get_apart_3(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.apart_3))

    def get_apart_4(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.apart_4))

    def get_s_link_parking(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.s_link_parking))

    def get_prking_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.parking_tittle)).text

    # Actions
    def click_projects(self):
        self.get_projects().click()
        print("Кликаем на кнопку проекты")

    def move_to_projects(self):
        self.actions.move_to_element(self.get_projects()).perform()
        print("Наводимся на проекты")

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

    def move_to_apart(self):
        self.actions.move_to_element(self.get_apart()).perform()
        print("Наводимся на квартиры")

    # Проверка подменю в ХЭДЕРЕ Actions

    def click_s_link_wrapper_9_from_header(self):
        self.get_s_link_wrapper_9_header().click()
        print("Кликаем на 9 пункт подменю")

    def click_s_link_wrapper_10_from_header(self):
        self.get_s_link_wrapper_10_header().click()
        print("Кликаем на 10 пункт подменю")

    def click_s_link_wrapper_11_from_header(self):
        self.get_s_link_wrapper_11_header().click()
        print("Кликаем на 11 пункт подменю")

    def click_s_link_wrapper_12_from_header(self):
        self.get_s_link_wrapper_12_header().click()
        print("Кликаем на 12 пункт подменю")

    def click_s_link_wrapper_13_from_header(self):
        self.get_s_link_wrapper_13_header().click()
        print("Кликаем на 13 пункт подменю")

    def click_s_link_wrapper_14_from_header(self):
        self.get_s_link_wrapper_14_header().click()
        print("Кликаем на 14 пункт подменю")

    def click_s_link_parking_from_header(self):
        self.get_s_link_parking().click()
        print("Кликаем на паркинг")

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

        # Проверка подменю в ХЭДЕРЕ Methods

    def check_wow_from_header(self):
        self.move_to_projects()
        self.click_s_link_wrapper_9_from_header()
        assert self.get_project_business_tittle() == "КАМЕРНЫЙ ДОМ НА БЕРЕГУ МОСКВЫ-РЕКИ"
        print("Проверяем заголовок")

    def check_ozerniy_from_header(self):
        self.move_to_projects()
        self.click_s_link_wrapper_10_from_header()
        assert self.get_project_business_tittle() == "ОАЗИС СПОКОЙСТВИЯ В МЕГАПОЛИСЕ"
        print("Проверяем заголовок")

    def check_dnv_from_header(self):
        self.move_to_projects()
        self.click_s_link_wrapper_11_from_header()
        assert self.get_project_dnv_check() == "Санкт-Петербург"
        print("Проверяем что попали на нужную страницу")

    def check_princip_from_header(self):
        self.move_to_projects()
        self.click_s_link_wrapper_12_from_header()
        assert self.get_project_comfort_tittle() == "ПРИНЦИП"
        print("Проверяем заголовок")

    def check_zvezdniy_from_header(self):
        self.move_to_projects()
        self.click_s_link_wrapper_9_from_header()
        assert self.get_project_comfort_tittle() == "Звездный"
        print("Проверяем заголовок")

    def check_union_from_header(self):
        self.move_to_projects()
        self.click_s_link_wrapper_10_from_header()
        assert self.get_project_comfort_tittle() == "Юнион"
        print("Проверяем заголовок")

    def check_avtorskiy_from_header(self):
        self.move_to_projects()
        self.click_s_link_wrapper_11_from_header()
        assert self.get_project_comfort_tittle() == "Авторский"
        print("Проверяем заголовок")

    def check_kolumb_from_header(self):
        self.move_to_projects()
        self.click_s_link_wrapper_12_from_header()
        assert self.get_project_comfort_tittle() == "Колумб"
        print("Проверяем заголовок")

    def check_sersib_from_header(self):
        self.move_to_projects()
        self.click_s_link_wrapper_13_from_header()
        print(self.get_project_comfort_tittle())
        assert self.get_project_comfort_tittle() == "Сердце Сибири"
        print("Проверяем заголовок")

    def check_domashniy_from_header(self):
        self.move_to_projects()
        self.click_s_link_wrapper_14_from_header()
        assert self.get_project_comfort_tittle() == "Домашний"
        print("Проверяем заголовок")

    def check_sibsad_from_header(self):
        self.move_to_projects()
        self.click_s_link_wrapper_9_from_header()
        assert self.get_project_comfort_tittle() == "Сибирский сад"
        print("Проверяем заголовок")
