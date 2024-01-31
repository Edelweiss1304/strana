from base.base_class import Base
from selenium.webdriver.common.by import By


class Footer(Base):
    # Locators
    vk = "//footer//a[@href='https://vk.com/strana_com']"
    yt = ("//footer//a[@href='https://www.youtube.com/c/%D0%A1%D0%A2%D0%A0%D0%90%D0%9D%D0%90%D0%94%D0%B5%D0%B2%D0%B5%D0%BB%D0%BE%D0%BF%D0%BC%D0%B5%D0%BD%D1%82/']")
    ok = "//footer//a[@href='https://ok.ru/stranacom']"
    tg = "//footer//a[@href='https://t.me/strana_com']"

    corruption = "//footer//span[contains(text(),'Противодействие коррупции')]"
    corruption_button = "//button[@type='submit']//span[@class='s-button__hover-shell']"
    confidentiality = "//footer//span[contains(text(),'Политика конфиденциальности')]"

    app = "//footer//a[@href = 'https://appgallery.huawei.com/#/app/C103444111']"

    company = "//footer//span[contains(text(), 'КОМПАНИЯ')][1]"
    actions = "//footer//span[contains(text(), 'АКЦИИ')]"
    purchase = "//footer//span[contains(text(), 'ИПОТЕКА')]"
    contacts = "//footer//span[contains(text(), 'КОНТАКТЫ')]"
    commercial = "//footer//span[contains(text(), 'КОММЕРЦИЯ')]"
    documents = "//footer//span[contains(text(), 'ДОКУМЕНТЫ')][1]"
    projects = "//footer//span[contains(text(), 'ПРОЕКТЫ')]"
    flats = "//footer//span[contains(text(), 'КВАРТИРЫ')]"
    purchase_methods = "//footer//span[contains(text(), 'Способы покупки')]"

    company_tittle = "//h1[contains(text(),'О компании')]"
    actions_tittle = "//h1[contains(text(),'Акции')]"
    purchase_tittle = "//h1[contains(text(),'Ипотека')]"
    contacts_tittle = "//h1[contains(text(),'Контакты')]"
    documents_tittle = "//h1[contains(text(),'Проектные документы')]"
    confidentiality_tittle = "//h1[contains(text(),'Политика конфиденциальности')]"
    projects_tittle = "//h1[contains(text(),'Новостройки')]"
    flats_tittle = "//h1[contains(text(),'Квартиры')]"
    purchase_methods_tittle = "//p[contains(text(),'Способы покупки')]"

    company_min = "//span[@class='currentValue_J0-2A'][contains(text(),'КОМПАНИЯ')][1]"
    land_owners = "//footer//span[contains(text(), 'Застройщикам и владельцам земли')]"
    tenders = "//footer//span[contains(text(), 'Тендеры')]"
    bureau = "//footer//span[contains(text(), 'Архитектурное бюро')]"

    # Getters
    def get_vk(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.vk))

    def get_yt(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.yt))

    def get_ok(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.ok))

    def get_tg(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.tg))

    def get_corruption(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.corruption))

    def get_corruption_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.corruption_button))

    def get_confidentiality(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.confidentiality))

    def get_app(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.app))

    def get_company(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.company))

    def get_company_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.company_tittle))

    def get_actions(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.actions))

    def get_actions_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.actions_tittle))

    def get_purchase(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.purchase))

    def get_purchase_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.purchase_tittle))

    def get_contacts(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.contacts))

    def get_contacts_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.contacts_tittle))

    def get_commercial(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.commercial))

    def get_documents(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.documents))

    def get_documents_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.documents_tittle))

    def get_company_min(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.company_min))

    def get_land_owners(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.land_owners))

    def get_tenders(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.tenders))

    def get_bureau(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.bureau))

    def get_confidentiality_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.confidentiality))

    def get_projects(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.projects))

    def get_projects_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.projects_tittle))

    def get_flats(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.flats))

    def get_flats_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.flats_tittle))

    def get_purchase_methods(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.purchase_methods))

    def get_purchase_methods_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.purchase_methods_tittle))


