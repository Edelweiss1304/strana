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
    more = "//button[contains(text(),'Еще')]"
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

    menu_button = "//button[@id='account']"
    menu_profile_agent = "//div[@class='v-list-item__title']//div[contains(text(), 'Профиль агента')]"
    agent_profile_poup_up = "//h2[contains(text(),'Профиль агента')]"
    menu_profile_representative = "//div[@class='v-list-item__title']//div[contains(text(), 'Профиль представителя')]"
    representative_profile_poup_up = "//h2[contains(text(),'Профиль представителя агентства')]"
    menu_profile_agency = "//div[@class='v-list-item__title']//div[contains(text(), 'Профиль агентства')]"
    agency_profile_poup_up = "//h2[contains(text(),'Профиль агентства')]"
    menu_loyalty_program = "//div[@class='v-list-item__title']//div[contains(text(), 'Программа лояльности')]"
    menu_exit = "//div[@class='v-list-item__title']//div[contains(text(), 'Выход')]"
    menu_exit_check = "//h1[contains(text(),'Вход в кабинет')]"
    close_poup_up = "//button[@id='drawer-close']"

    burger_menu_button = "//button[contains(@class, 'btn-reset') and contains(@class, 'TheHeaderBurger_Vxpqv') and contains(@class, 'menuBtn_oY2LB')]"
    burger_faq = "//a[.//span[contains(text(), 'Часто задаваемые вопросы')]]"
    burger_faq_tittle = "//div[contains(text(), 'Часто задаваемые вопросы')]"
    burger_deals = "//a[.//span[contains(text(), 'Сделки')]]"
    burger_flats = "//a[.//span[contains(text(), 'Выбор квартиры')]]"
    burger_news = "//a[.//span[contains(text(), 'Новости и акции')]]"
    burger_loyalty = "//a[.//span[contains(text(), 'Программа лояльности')]]"
    burger_calendar = "//a[.//span[contains(text(), 'Календарь')]]"
    burger_documents = "//a[.//span[contains(text(), 'Документы')]]"
    burger_interaction = "//a[.//span[contains(text(), 'Взаимодействие')]]"
    burger_agents = "//a[.//span[contains(text(), 'Агенты')]]"
    burger_agents_tittle = "//h1[contains(text(),'Агенты')]"
    burger_projects = "//a[.//span[contains(text(), 'Проекты')]]"
    burger_projects_tittle = "//span[contains(text(),'Новостройки')]"
    burger_flats_site = "//a[.//span[contains(text(), 'Квартиры')]]"
    burger_flats_site_tittle = "//h1[.//span[contains(text(),'Квартиры')]]"
    burger_commercial = "//a[.//span[contains(text(), 'Коммерция')]]"
    burger_commercial_tittle = "//h2[contains(text(),'Коммерческие помещения в других городах')]"
    burger_project_documents = "//a[.//span[contains(text(), 'Проектные документы')]]"
    burger_project_documents_tittle = "//h1[.//span[contains(text(),'Проектные документы')]]"
    burger_contacts = "//a[.//span[contains(text(), 'Контакты')]]"
    burger_contacts_tittle = "//h1[contains(text(),'Контакты')]"

    # Getter's
    def get_more(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.more))

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

    def get_menu_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.menu_button))

    def get_menu_profile_agent(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.menu_profile_agent))

    def get_agent_profile_poup_up(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.agent_profile_poup_up))

    def get_menu_profile_representative(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.menu_profile_representative))

    def get_representative_profile_poup_up(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.representative_profile_poup_up))

    def get_menu_profile_agency(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.menu_profile_agency))

    def get_menu_loyalty_program(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.menu_loyalty_program))

    def get_menu_exit(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.menu_exit))

    def get_menu_exit_check(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.menu_exit_check))

    def get_close_poup_up(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.close_poup_up))

    def get_agency_profile_poup_up(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.agency_profile_poup_up))

    def get_burger_menu_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_menu_button))

    def get_burger_faq(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_faq))

    def get_burger_faq_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_faq_tittle))

    def get_burger_deals(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_deals))

    def get_burger_flats(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_flats))

    def get_burger_news(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_news))

    def get_burger_loyalty(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_loyalty))

    def get_burger_calendar(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_calendar))

    def get_burger_documents(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_documents))

    def get_burger_interaction(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_interaction))

    def get_burger_agents(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_agents))

    def get_burger_agents_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_agents_tittle))

    def get_burger_projects(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_projects))

    def get_burger_projects_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_projects_tittle))

    def get_burger_flats_site(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_flats_site))

    def get_burger_flats_site_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_flats_site_tittle))

    def get_burger_commercial(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_commercial))

    def get_burger_commercial_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_commercial_tittle))

    def get_burger_project_documents(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_project_documents))

    def get_burger_project_documents_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_project_documents_tittle))

    def get_burger_contacts(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_contacts))

    def get_burger_contacts_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.burger_contacts_tittle))
