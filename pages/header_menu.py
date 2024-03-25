from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Burger(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.Base = Base
        self.driver = driver
        self.actions = ActionChains(driver)

    # Локаторы бургера
    menu_button = "//span[@class='s-shift-text__value'][contains(text(),'Меню')]"
    projects = "//a[contains (text(), 'Проекты')]"
    flats = "//a[contains (text(), 'Квартиры')]"
    commercial = "//a[contains (text(), 'Коммерция')]"

    VK = "//a[@href='https://vk.com/strana_com']"
    OK = "//a[@href='https://ok.ru/stranacom']"
    YT = ("//a[@href='https://www.youtube.com/c/%D0%A1%D0%A2%D0%A0%D0%90%D0%9D%D0%90%D0%94%D0%B5%D0%B2%D0%B5%D0%BB%D0%BE%D0%BF%D0%BC%D0%B5%D0%BD%D1%82/']")
    TG = "//a[@href='https://t.me/strana_com']"

    company = "//a[contains(text(),'О компании')]"
    purchase = "//a[contains(text(),'Способы покупки')]"
    documents = "//a[contains(text(),'Документы')]"
    vacancy = "//a[contains(text(),'Вакансии')]"
    offers = "//a[contains(text(),'Акции')]"
    news = "//a[contains(text(),'Новости')]"
    progress = "//a[contains(text(),'Ход строительства')]"

    bonus = "//a[contains(text(),'Страна.Бонус')]"
    investors = "//a[contains(text(),'Инвесторам')]"
    agents = "//a[contains(text(),'Агентам и агентствам')]"
    partners = "//a[contains(text(),'Партнерам')]"
    tenders = "//a[contains(text(),'Тендеры')]"
    contacts = "//a[contains(text(),'Контакты')]"
    sale = "//a[contains(text(),'SALE %')]"
    parking = "//a[contains(text(),'Паркинги и кладовые')]"

    # Элементы страниц для assert
    projects_tittle = "//span[contains(text(),'Новостройки')]"
    flats_tittle = "//h1[span[contains(text(), 'Квартиры')]]"
    news_tittle = "//h1[contains(text(),'Новости')]"
    company_tittle = "//h1[contains(text(),'О компании')]"
    purchase_tittle = "//p[contains(text(),'Способы покупки')]"
    vacancy_tittle = "//span[contains(text(),'Смотреть вакансии')]"
    vacancy_search = "//div[contains(text(),'Любое направление')]"
    bonus_tittle = "//span[contains(text(),'.Бонус')]"
    investors_tittle = "//h1[contains(text(),'Инвесторам')]"
    partners_tittle = "//h1[contains(text(),'Партнеры')]"
    tenders_tittle = "//h3[contains(text(),'Заключить договор проще, чем ты думаешь')]"
    contacts_tittle = "//h1[contains(text(),'Контакты')]"
    offers_tittle = "//h1[contains(text(),'Акции')]"
    progress_tittle = "//h1[contains(text(),'Ход строительства')]"
    documents_tittle = "//h1[contains(text(),'Проектные документы')]"
    commercial_tittle = "//h1[contains(text(),'Коммерческая недвижимость')]"
    parking_tittle = "//h1[contains(text(),'Паркинги')]"

    # Getters

    def get_menu_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.menu_button))

    def get_projects(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.projects))

    def get_flats(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.flats))

    def get_commercial(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.commercial))

    def get_vk(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.VK))

    def get_ok(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.OK))

    def get_yt(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.YT))

    def get_tg(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.TG))

    def get_company(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.company))

    def get_purchase(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.purchase))

    def get_documents(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.documents))

    def get_vacancy(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.vacancy))

    def get_offers(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.offers))

    def get_news(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.news))

    def get_progress(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.progress))

    def get_bonus(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.bonus))

    def get_investors(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.investors))

    def get_agents(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.agents))

    def get_partners(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.partners))

    def get_tenders(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.tenders))

    def get_contacts(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.contacts))

    def get_sale(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.sale))

    def get_parking(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.parking))
    # Getters tittle

    def get_projects_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.projects_tittle)).text

    def get_flats_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.flats_tittle)).text

    def get_news_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.news_tittle)).text

    def get_company_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.company_tittle)).text

    def get_purchase_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.purchase_tittle)).text

    def get_vacancy_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.vacancy_tittle))

    def get_vacancy_search(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.vacancy_search)).text

    def get_bonus_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.bonus_tittle)).text

    def get_investors_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.investors_tittle)).text

    def get_partners_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.partners_tittle)).text

    def get_tenders_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.tenders_tittle)).text

    def get_contacts_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.contacts_tittle)).text

    def get_offers_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.offers_tittle)).text

    def get_progress_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.progress_tittle)).text

    def get_documents_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.documents_tittle)).text

    def get_commercial_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.commercial_tittle)).text

    def get_parking_tittle(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.parking_tittle)).text
