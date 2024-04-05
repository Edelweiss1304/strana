from base.base_class import Base
from selenium.webdriver.common.by import By
import time
from pages.header_links import Header
import testit


class BrokerRegistration(Base):
    # Locators
    first_registration_button = "//a[contains(text(),'Зарегистрироваться')]"
    switch_agent_agency = "//a[.//span[normalize-space()='Агентство']]"

    inn_for_agency = "//label[normalize-space()='ИНН']/preceding-sibling::input"
    name_agency = "//label[normalize-space()='Название агентства']/preceding-sibling::input"
    city_agency = "//label[normalize-space()='Город деятельности']/preceding-sibling::input"
    agency_doc_1 = "//label[contains(text(), 'Карточка предприятия')]/preceding-sibling::input"
    agency_doc_2 = "//label[contains(text(),'Доверенность')]/preceding-sibling::input"
    position_field_registration = "//label[normalize-space()='Должность администратора']/following-sibling::div[@class='v-select__selections']/input"
    position_field_registration_director = "//div[contains(@class, 'v-list-item__title') and normalize-space()='Директор']"

    inn_for_agent = "//label[text()='ИНН агентства']/preceding-sibling::input"
    continue_button_for_agent_1 = "//button[.//span[contains(text(), 'Продолжить')]]"
    surname_registration_field = "//label[normalize-space()='Фамилия']/preceding-sibling::input"
    name_rigistration_field = "//label[normalize-space()='Имя']/preceding-sibling::input"
    second_name_rigistration_field = "//label[normalize-space()='Отчество']/preceding-sibling::input"
    phone_rigistration_field = "//label[normalize-space()='Телефон']/preceding-sibling::input"
    email_rigistration_field = "//label[normalize-space()='E-mail']/preceding-sibling::input"
    password_rigistration_field = "//label[normalize-space()='Пароль']/preceding-sibling::input"
    second_password_rigistration_field = "//label[normalize-space()='Повторите пароль']/preceding-sibling::input"
    fin_registration_button = "//button[.//span[normalize-space()='Зарегистрироваться']]"
    confirm_reglament_button = "//button[.//span[normalize-space()='Принимаю']]"

    # Getters
    def get_first_registration_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.first_registration_button))

    def get_inn_for_agent(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.inn_for_agent))

    def get_continue_button_for_agent_1(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.continue_button_for_agent_1))

    def get_surname_registration_field(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.surname_registration_field))

    def get_name_rigistration_field(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.name_rigistration_field))

    def get_second_name_rigistration_field(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.second_name_rigistration_field))

    def get_phone_rigistration_field(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.phone_rigistration_field))

    def get_email_rigistration_field(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.email_rigistration_field))

    def get_password_rigistration_field(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.password_rigistration_field))

    def get_second_password_rigistration_field(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.second_password_rigistration_field))

    def get_fin_registration_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.fin_registration_button))

    def get_confirm_reglament_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.confirm_reglament_button))

    def get_switch_agent_agency(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.switch_agent_agency))

    def get_inn_for_agency(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.inn_for_agency))

    def get_name_agency(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.name_agency))

    def get_city_agency(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.city_agency))

    def get_agency_doc_1(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.agency_doc_1))

    def get_agency_doc_2(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.agency_doc_2))

    def get_position_field_registration(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.position_field_registration))

    def get_position_field_registration_director(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.position_field_registration_director))
