import pytest
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import testit
from pages.flats import Flats


class Header(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.Base = Base
        self.driver = driver
        self.actions = ActionChains(driver)

    # Локаторы для кнопок в хэдере

    projects = "//span[@class='s-shift-text__value'][contains(text(),'Проекты')]"
    apart = "//span[@class='s-shift-text__value'][contains(text(),'Квартиры')]"
    commercial = "//span[@class='s-shift-text__value'][contains(text(),'Помещения')]"
    action = "//span[@class='s-shift-text__value'][contains(text(),'Акции')]"
    about = "//span[@class='s-shift-text__value'][contains(text(),'О компании')]"
    purchase_methods = "//span[@class='s-shift-text__value'][contains(text(),'Способы покупки')]"
    sale = "//span[@class='s-shift-text__value'][normalize-space()='SALE %']"
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
    project_comfort_tittle = ".project-hero__title"
    project_dnv_check = "(//div[@class='listLabel_Q6E55'][contains(text(),'Санкт-Петербург')])[1]"
    city_in_apart = "div[class='s-select s-select--string s-select--secondary s-select--large'] div[" \
                    "class='s-select__rendered']"
    s_link_parking = "//a[@href='/parking']"  # Паркинг

    text_color = "rgba(146, 39, 143, 1)"
    apart_0 = "//span[contains(text(),'Студия')]"
    apart_1 = "//span[normalize-space()='1']"
    apart_2 = "//span[normalize-space()='2']"
    apart_3 = "//span[normalize-space()='3']"
    apart_4 = "//span[normalize-space()='4+']"
    parking_tittle = "(//h1[@class='title_gewxY h3 text-base-500'][contains(text(),'Паркинг')])[1]"

    menu_button = "//span[@class='s-shift-text__value'][contains(text(),'Меню')]"
    news_tittle = "(//span[contains(text(),'Новости')])[1]"

    header_pop_up = "//div[@class='the-header-popup-menu the-header-popup-menu--theme-common']"

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

    def get_sale(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.sale))

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

    def get_menu_button(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.menu_button))

    def get_news_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.news_tittle)).text

    def get_header_pop_up(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.header_pop_up))

    # Actions
    with testit.step("Кликаем на проекты"):
        def click_projects(self):
            self.get_projects().click()
            print("Кликаем на кнопку проекты")

    def move_to_projects(self):
        self.actions.move_to_element(self.get_projects()).perform()
        self.get_header_pop_up()
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

    def click_sale(self):
        self.get_sale().click()
        print("Кликаем на кнопку sale")

    def move_to_apart(self):
        self.actions.move_to_element(self.get_apart()).perform()
        self.get_header_pop_up()
        print("Наводимся на квартиры")

    # Проверка подменю в ХЭДЕРЕ Actions

    def click_s_link_wrapper_8_from_header(self):
        locator = Base.get_s_link_wrapper_locator(8)
        Base.get_element_clickable(self.driver, (By.XPATH, locator)).click()
        print("Кликаем на 9 пункт подменю")

    def click_s_link_wrapper_9_from_header(self):
        locator = Base.get_s_link_wrapper_locator(9)
        Base.get_element_clickable(self.driver, (By.XPATH, locator)).click()
        print("Кликаем на 9 пункт подменю")

    def click_s_link_wrapper_10_from_header(self):
        locator = Base.get_s_link_wrapper_locator(10)
        Base.get_element_clickable(self.driver, (By.XPATH, locator)).click()
        print("Кликаем на 10 пункт подменю")

    def click_s_link_wrapper_11_from_header(self):
        locator = Base.get_s_link_wrapper_locator(11)
        Base.get_element_clickable(self.driver, (By.XPATH, locator)).click()
        print("Кликаем на 11 пункт подменю")

    def click_s_link_wrapper_12_from_header(self):
        locator = Base.get_s_link_wrapper_locator(12)
        Base.get_element_clickable(self.driver, (By.XPATH, locator)).click()
        print("Кликаем на 12 пункт подменю")

    def click_s_link_wrapper_13_from_header(self):
        locator = Base.get_s_link_wrapper_locator(13)
        Base.get_element_clickable(self.driver, (By.XPATH, locator)).click()
        print("Кликаем на 13 пункт подменю")

    def click_s_link_wrapper_14_from_header(self):
        locator = Base.get_s_link_wrapper_locator(14)
        Base.get_element_clickable(self.driver, (By.XPATH, locator)).click()
        print("Кликаем на 14 пункт подменю")

    def click_s_link_wrapper_15_from_header(self):
        locator = Base.get_s_link_wrapper_locator(15)
        Base.get_element_clickable(self.driver, (By.XPATH, locator)).click()
        print("Кликаем на 15 пункт подменю")

    def click_s_link_parking_from_header(self):
        self.get_s_link_parking().click()
        print("Кликаем на паркинг")

        # Methods

    def check_projects(self):
        with testit.step("Нажимаем на проекты"):
            self.click_projects()
        with testit.step("Проверяем заголовок страницы"):
            assert self.get_projects_check() == "Проекты"
            print("Проверяем заголовок")

    def check_apart(self):
        with testit.step("Нажимаем на квартиры"):
            self.click_apart()
        with testit.step("Проверяем заголовок страницы"):
            assert self.get_apart_check() == "Подобрать квартиру"
        print("Проверяем заголовок")

    def check_commercial(self):
        with testit.step("Нажимаем на Коммерцию"):
            self.click_commercial()
        with testit.step("Проверяем заголовок страницы"):
            assert self.get_projects_check() == "Проекты"
        print("Проверяем заголовок")

    def check_actions(self):
        with testit.step("Нажимаем на Акции"):
            self.click_action()
        with testit.step("Проверяем заголовок страницы"):
            assert self.get_actions_check() == "Акции"
        print("Проверяем заголовок")

    def check_about(self):
        with testit.step("Нажимаем О нас"):
            self.click_about()
        with testit.step("Проверяем заголовок страницы"):
            assert self.get_about_check() == "О компании"
        print("Проверяем заголовок")

    def check_purchase_methods(self):
        with testit.step("Нажимаем методы покупки"):
            self.click_purchase_methods()
        with testit.step("Проверяем заголовок страницы"):
            assert self.get_purchase_methods_check() == "Материнский капитал"
        print("Проверяем заголовок")

    def check_sale(self):
        with testit.step("Нажимаем sale"):
            self.click_sale()
        with testit.step("Проверяем заголовок страницы"):
            assert self.get_apart_check() == "Подобрать квартиру"
        print("Проверяем заголовок")

        # Проверка подменю в ХЭДЕРЕ Methods

    def check_wow_from_header(self):
        with testit.step("Наводимся на проекты"):
            self.move_to_projects()
        with testit.step("Кликаем на WOW"):
            self.click_s_link_wrapper_8_from_header()
        with testit.step("Проверяем, что попали на WOW"):
            assert self.get_project_business_tittle() == "КАМЕРНЫЙ ДОМ НА БЕРЕГУ МОСКВЫ-РЕКИ"
            print("Проверяем заголовок")

    def check_ozerniy_from_header(self):
        with testit.step("Наводимся на проекты"):
            self.move_to_projects()
        with testit.step("Кликаем на Озерный"):
            self.click_s_link_wrapper_9_from_header()
        with testit.step("Проверяем, что попали на Озерный"):
            assert self.get_project_business_tittle() == "ОАЗИС СПОКОЙСТВИЯ В МЕГАПОЛИСЕ"
            print("Проверяем заголовок")

    def check_dnv_from_header(self):
        with testit.step("Наводимся на проекты"):
            self.move_to_projects()
        with testit.step("Кликаем на ДнВ"):
            self.click_s_link_wrapper_9_from_header()
        with testit.step("Проверяем, что попали на ДнВ"):
            assert self.get_project_dnv_check() == "Санкт-Петербург"
            print("Проверяем что попали на нужную страницу")

    def check_zvezdniy_from_header(self):
        with testit.step("Наводимся на проекты"):
            self.move_to_projects()
        with testit.step("Кликаем на Звездный"):
            self.click_s_link_wrapper_10_from_header()
        with testit.step("Проверяем, что попали Звездный"):
            assert self.get_project_comfort_tittle() == "Звездный"
            print("Проверяем заголовок")

    def check_union_from_header(self):
        with testit.step("Наводимся на проекты"):
            self.move_to_projects()
        with testit.step("Кликаем на Юнион"):
            self.click_s_link_wrapper_9_from_header()
        with testit.step("Проверяем, что попали Юнион"):
            assert self.get_project_comfort_tittle() == "Юнион"
            print("Проверяем заголовок")

    def check_avtorskiy_from_header(self):
        with testit.step("Наводимся на проекты"):
            self.move_to_projects()
        with testit.step("Кликаем на Авторский"):
            self.click_s_link_wrapper_11_from_header()
        with testit.step("Проверяем, что попали на Авторский"):
            assert self.get_project_comfort_tittle() == "Авторский"
            print("Проверяем заголовок")

    def check_kolumb_from_header(self):
        with testit.step("Наводимся на проекты"):
            self.move_to_projects()
        with testit.step("Кликаем на Колумб"):
            self.click_s_link_wrapper_13_from_header()
        with testit.step("Проверяем, что попали в Колумб"):
            assert self.get_project_comfort_tittle() == "Колумб"
            print("Проверяем заголовок")

    def check_sersib_from_header(self):
        with testit.step("Наводимся на проекты"):
            self.move_to_projects()
        with testit.step("Кликаем на Сердце Сибири"):
            self.click_s_link_wrapper_15_from_header()
        with testit.step("Проверяем, что попали на Сердце Сибири"):
            assert self.get_project_comfort_tittle() == "Сердце Сибири"
            print("Проверяем заголовок")

    def check_domashniy_from_header(self):
        with testit.step("Наводимся на проекты"):
            self.move_to_projects()
        with testit.step("Кликаем на Домашний"):
            self.click_s_link_wrapper_14_from_header()
        with testit.step("Проверяем, что попали на Домашний"):
            assert self.get_project_comfort_tittle() == "Домашний"
            print("Проверяем заголовок")

    def check_eb_from_header(self):
        with testit.step("Наводимся на проекты"):
            self.move_to_projects()
        with testit.step("Кликаем на ЕБ"):
            self.click_s_link_wrapper_12_from_header()
        with testit.step("Првоеряем, что попали на ЕБ"):
            assert self.get_project_comfort_tittle() == "Европейский берег 2.0"
            print("Проверяем заголовок")

    def check_sibsad_from_header(self):
        with testit.step("Наводимся на проекты"):
            self.move_to_projects()
        with testit.step("Кликаем на Сибирский Сад"):
            self.click_s_link_wrapper_9_from_header()
        with testit.step("Проверяем, что попали на Сибирский Сад"):
            assert self.get_project_comfort_tittle() == "Сибирский сад"
            print("Проверяем заголовок")
