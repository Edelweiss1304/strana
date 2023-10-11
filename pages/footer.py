from base.base_class import Base
from selenium.webdriver.common.by import By


class Footer(Base):
    # Locators
    vk = "//footer//a[@href='https://vk.com/strana_com']"
    yt = ("//footer//a[@href='https://www.youtube.com/c/%D0%A1%D0%A2%D0%A0%D0%90%D0%9D%D0%90%D0%94%D0%B5%D0%B2%D0%B5%D0%BB%D0%BE%D0%BF%D0%BC%D0%B5%D0%BD%D1%82/']")
    ok = "//footer//a[@href='https://ok.ru/stranacom']"
    tg = "//footer//a[@href='https://t.me/strana_com']"

    corruption = "//footer//span[contains(text(),'Противодействие коррупции')]"
    confidentiality = "//footer//span[contains(text(),'Политика конфиденциальности')]"

    app = "//footer//a[@href = 'https://appgallery.huawei.com/#/app/C103444111']"

    company = "//footer//span[contains(text(), 'КОМПАНИЯ')][1]"
    actions = "//footer//span[contains(text(), 'АКЦИИ')]"
    purchase = "//footer//span[contains(text(), 'ИПОТЕКА')]"
    contacts = "//footer//span[contains(text(), 'КОНТАКТЫ')]"
    commercial = "//footer//span[contains(text(), 'КОММЕРЦИЯ')]"
    documents = "//footer//span[contains(text(), 'ДОКУМЕНТЫ')]"

    company_min = "//footer//span[contains(text(), 'КОМПАНИЯ')][2]"
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

    def get_confidentiality(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.confidentiality))

    def get_app(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.app))

    def get_company(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.company))

    def get_actions(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.actions))

    def get_purchase(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.purchase))

    def get_contacts(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.contacts))

    def get_commercial(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.commercial))

    def get_documents(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.documents))

    def get_company_min(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.company_min))

    def get_land_owners(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.land_owners))

    def get_tenders(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.tenders))

    def get_bureau(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.bureau))


