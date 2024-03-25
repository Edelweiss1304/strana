from pages.header_links import Header
from base.base_class import Base
from pages.url import URLS_MAIN
import testit


# MSK
@testit.displayName('Проверка кнопки проекты мск')
@testit.description('Проверка кнопки проекты мск')
def test_msk_header_projects(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_projects()


@testit.displayName("Проверка кнопки квартиры мск")
@testit.description("Проверка кнопки квартиры мск")
def test_msk_header_apart(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_apart_1()


@testit.displayName("Проверка кнопки помещения мск")
@testit.description("Проверка кнопки помещения мск")
def test_msk_header_commercial(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_commercial()
    with testit.step("Проверяем url страницы"):
        assert driver.current_url.endswith('/projects/commercial/')


@testit.displayName("Проверка кнопки акции мск")
@testit.description("Проверка кнопки акции мск")
def test_msk_header_actions(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_actions()


@testit.displayName("Проверка кнопки о компании мск")
@testit.description("Проверка кнопки о компании мск")
def test_msk_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_about()


@testit.displayName("Проверка кнопки способы покупки мск")
@testit.description("Проверка кнопки способы покупки мск")
def test_msk_header_purchase_methods(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_purchase_methods()


# MO


@testit.displayName("Проверка кнопки акции мо")
@testit.description("Проверка кнопки акции мо")
def test_mo_header_actions(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_mo'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_actions()


@testit.displayName("Проверка кнопки о компании мо")
@testit.description("Проверка кнопки о компании мо")
def test_mo_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_mo'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_about()


@testit.displayName("Проверка кнопки вакансии мо")
@testit.description("Проверка кнопки вакансии мо")
def test_mo_header_vacancy(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_mo'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
    with testit.step("Кликаем на вакансии"):
        head.get_vacancy().click()
    with testit.step("Проверяем, что попали на вакнсии"):
        head.get_vacancy_check()

    # SPB


@testit.displayName("Проверка кнопки проекты спб")
@testit.description("Проверка кнопки проекты спб")
def test_spb_header_projects(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_projects()


@testit.displayName("Проверка кнопки квартиры спб")
@testit.description("Проверка кнопки квартиры спб")
def test_spb_header_apart(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_apart()


@testit.displayName("Проверка кнопки помещения спб")
@testit.description("Проверка кнопки помещения спб")
def test_spb_header_commercial(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_commercial()
    with testit.step("Проверяем url страницы"):
        assert driver.current_url.endswith('/projects/commercial/')


@testit.displayName("Проверка кнопки акции спб")
@testit.description("Проверка кнопки акции спб")
def test_spb_header_actions(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_actions()


@testit.displayName("Проверка кнопки о нас спб")
@testit.description("Проверка кнопки о нас спб")
def test_spb_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_about()


# @testit.displayName("Проверка кнопки методы покупки спб")
# @testit.description("Проверка кнопки методы покупки спб")
# def test_spb_header_purchase_methods(driver):
#     head = Header(driver)
#     with testit.step("Открываем главную страницу"):
#         Base.open_page(driver, URLS_MAIN['url_spb'])
#         base_inst = Base(driver)
#         base_inst.click_accept_city()
#         head.check_purchase_methods()

    # EKB


@testit.displayName("Проверка кнопки проекты екб")
@testit.description("Проверка кнопки проекты екб")
def test_ekb_header_projects(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_projects()


@testit.displayName("Проверка кнопки квартиры екб")
@testit.description("Проверка кнопки квартиры екб")
def test_ekb_header_apart(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_apart_1()


@testit.displayName("Проверка кнопки помещения екб")
@testit.description("Проверка кнопки помещения екб")
def test_ekb_header_commercial(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_commercial()
    with testit.step("Проверяем url страницы"):
        assert driver.current_url.endswith('/projects/commercial/')


@testit.displayName("Проверка кнопки акции екб")
@testit.description("Проверка кнопки акции екб")
def test_ekb_header_actions(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_actions()


@testit.displayName("Проверка кнопки о компании екб")
@testit.description("Проверка кнопки о компании екб")
def test_ekb_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_about()


@testit.displayName("Проверка кнопки онлайн покупка екб")
@testit.description("Проверка кнопки онлайн покупка екб")
def test_ekb_header_purchase_methods(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_purchase_methods()

    # TMN


@testit.displayName("Проверка кнопки проекты тмн")
@testit.description("Проверка кнопки проекты тмн")
def test_tmn_header_projects(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_projects()


@testit.displayName("Проверка кнопки квартиры тмн")
@testit.description("Проверка кнопки квартиры тмн")
def test_tmn_header_apart(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_apart_1()


@testit.displayName("Проверка кнопки помещения тмн")
@testit.description("Проверка кнопки помещения тмн")
def test_tmn_header_commercial(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_commercial()
    with testit.step("Проверяем url страницы"):
        assert driver.current_url.endswith('/projects/commercial/')


@testit.displayName("Проверка кнопки акции тмн")
@testit.description("Проверка кнопки акции тмн")
def test_tmn_header_actions(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_actions()


@testit.displayName("Проверка кнопки о компании тмн")
@testit.description("Проверка кнопки о компании тмн")
def test_tmn_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_about()


@testit.displayName("Проверка кнопки онлайн покупка тмн")
@testit.description("Проверка кнопки онлайн покупка тмн")
def test_tmn_header_purchase_methods(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_purchase_methods()

    # NSK


@testit.displayName("Проверка кнопки о компании нск")
@testit.description("Проверка кнопки о компании")
def test_nsk_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_nsk'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
        head.check_about()


@testit.displayName("Проверка кнопки Вакансии нск")
@testit.description("Проверка кнопки Вакансии нск")
def test_nsk_vacancy(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_nsk'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
    with testit.step("Кликаем на вакансии"):
        head.get_vacancy().click()
    with testit.step("Проверяем, что попали на вакнсии"):
        head.get_vacancy_check()
