from base.base_class import Base
from selenium.webdriver.common.by import By


class Lk(Base):
    # Locators
    uniqueness_button = "//div[contains(text(), 'Проверить клиента на уникальность')]"
    uniqueness_button_deal = "//button[.//span[contains(text(), 'Создать сделку')]]"
    uniqueness_input = "//label[text()='Номер телефона']/../input"
    uniqueness_button_popup = "//span[contains(text(), 'Проверить')]"
    result_uniqueness = "//div[contains(text(), 'Уникальный')]"

    # Top_menu
    # Locators
    clients = "//a[.//span[contains(text(), 'Клиенты')]]"
    agents = "//a[.//span[contains(text(), 'Агенты')]]"
    documents = "//a[.//span[contains(text(), 'Документы')]]"
    apart = "//a[.//span[contains(text(), 'Выбор квартиры')]]"
    calendar = "//a[.//span[contains(text(), 'Календарь')]]"
    loyalty = "//a[.//span[contains(text(), 'Программа лояльности')]]"
    interaction = "//a[.//span[contains(text(), 'Взаимодействие')]]"
    news = "//a[.//span[contains(text(), 'Новости и акции')]]"

    # Headers
    clients_h = "//h1[contains(text(),'Клиенты')]"
    agents_h = "//h1[contains(text(),'Агенты')]"
    documents_h = "//h1[contains(text(),'Документы')]"
    apart_h = "//div[contains(text(),'Выберите ЖК')]"
    calendar_h = "//h1[contains(text(),'Календарь')]"
    loyalty_h = "//h4[contains(text(),'Программа лояльности')]"
    interaction_h = "//h1[contains(text(),'Взаимодействие')]"
    news_h = "//h1[contains(text(),'Новости')]"

    uniqueness_city = "//label[normalize-space()='Город']/following-sibling::div[@class='v-select__selections']/input"
    uniqueness_city_tmn = "//div[contains(@class, 'v-list-item__title') and normalize-space()='Тюмень']"
    uniqueness_zk = "//label[normalize-space()='Интересующие ЖК']/following-sibling::div[@class='v-select__selections']/input"
    uniqueness_zk_domashniy = "//div[contains(@class, 'v-list-item__title') and normalize-space()='Домашний']"
    uniqueness_surname = "//label[normalize-space()='Фамилия']/preceding-sibling::input"
    uniqueness_name = "//label[normalize-space()='Имя']/preceding-sibling::input"
    uniqueness_second_name = "//label[normalize-space()='Отчество']/preceding-sibling::input"
    uniqueness_consultation = "//label[normalize-space()='Тип консультации']/following-sibling::div[@class='v-select__selections']/input"
    uniqueness_consultation_office = "//div[contains(@class, 'v-list-item__title') and normalize-space()='Встреча с клиентом в офисе']"
    uniqueness_comment = "//label[normalize-space()='Комментарий']/preceding-sibling::input"
    uniqueness_fin_button = "//button[.//span[normalize-space()='Закрепить']]"

    # Getter's
    def get_uniqueness_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_button))

    def get_uniqueness_button_deal(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_button_deal))

    def get_uniqueness_input(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_input))

    def get_uniqueness_button_popup(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_button_popup))

    def get_result_uniqueness(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.result_uniqueness))

    def get_uniqueness_city(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_city))

    def get_uniqueness_city_tmn(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_city_tmn))

    def get_uniqueness_zk(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_zk))

    def get_uniqueness_zk_domashniy(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_zk_domashniy))

    def get_uniqueness_surname(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_surname))

    def get_uniqueness_name(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_name))

    def get_uniqueness_second_name(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_second_name))

    def get_uniqueness_consultation(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_consultation))

    def get_uniqueness_consultation_office(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_consultation_office))

    def get_uniqueness_comment(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_comment))

    def get_uniqueness_fin_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.uniqueness_fin_button))

    def get_clients(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.clients))

    def get_agents(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.agents))

    def get_documents(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.documents))

    def get_apart(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.apart))

    def get_calendar(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.calendar))

    def get_loyalty(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.loyalty))

    def get_interaction(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.interaction))

    def get_news(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.news))

    def get_clients_h(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.clients_h))

    def get_agents_h(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.agents_h))

    def get_documents_h(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.documents_h))

    def get_apart_h(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.apart_h))

    def get_calendar_h(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.calendar_h))

    def get_loyalty_h(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.loyalty_h))

    def get_interaction_h(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.interaction_h))

    def get_news_h(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.news_h))
