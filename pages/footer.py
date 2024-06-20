from base.base_class import Base
from selenium.webdriver.common.by import By


class Footer(Base):
    # Locators
    vk = "//a[@href='https://vk.com/strana_com' and @target='_blank' and contains(@class, 'footer__social-link')]"
    yt = "//a[@href='https://www.youtube.com/c/%D0%A1%D0%A2%D0%A0%D0%90%D0%9D%D0%90%D0%94%D0%B5%D0%B2%D0%B5%D0%BB%D0%BE%D0%BF%D0%BC%D0%B5%D0%BD%D1%82/' and @target='_blank' and contains(@class, 'footer__social-link')]"
    ok = "//a[@href='https://ok.ru/stranacom' and @target='_blank' and contains(@class, 'footer__social-link')]"
    tg = "//a[@href='https://t.me/strana_com' and @target='_blank' and contains(@class, 'footer__social-link')]"

    corruption = "//footer//span[contains(text(),'Противодействие коррупции')]"
    corruption_button = "//button[@type='submit']//span[@class='s-button__hover-shell']"
    confidentiality = "//span[@class='s-shift-link__value'][contains(text(),'Политика конфиденциальности')]"

    app = "//footer//a[@href = 'https://appgallery.huawei.com/#/app/C103444111']"

    company = "//span[@class='s-shift-link__value'][contains(text(),'О компании')]"
    actions = "//span[@class='s-shift-link__value'][contains(text(),'Акции')]"
    purchase = "//span[@class='s-shift-link__value'][contains(text(),'Ипотека')]"
    contacts = "//span[@class='s-shift-link__value'][contains(text(),'Контакты')]"
    commercial = "//footer//span[contains(text(), 'КОММЕРЦИЯ')]"
    documents = "//span[@class='s-shift-link__value'][contains(text(),'Документы')]"
    projects = "//span[@class='s-shift-link__value'][contains(text(),'Проекты')]"
    flats = "//span[@class='s-shift-link__value'][contains(text(),'Квартиры')]"
    purchase_methods = "//span[@class='s-shift-link__value'][contains(text(),'Способы покупки')]"

    company_tittle = "//h1[contains(text(),'О компании')]"
    actions_tittle = "//h1[contains(text(),'Акции')]"
    purchase_tittle = "//h1[contains(text(),'Ипотека')]"
    contacts_tittle = "//h1[contains(text(),'Контакты')]"
    documents_tittle = "//h1/span[normalize-space()='Проектные документы']"
    confidentiality_tittle = "//h1[contains(text(),'Политика конфиденциальности')]"
    projects_tittle = "//span[contains(text(),'Новостройки')]"
    flats_tittle = "//h1[contains(text(),'Квартиры')]"
    flats_tittle_1 = "(//span[normalize-space(.)='Квартиры'])[1]"
    purchase_methods_tittle = "//p[contains(text(),'Способы покупки')]"

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

    def get_flats_tittle_1(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.flats_tittle_1))

    def get_purchase_methods(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.purchase_methods))

    def get_purchase_methods_tittle(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.purchase_methods_tittle))


