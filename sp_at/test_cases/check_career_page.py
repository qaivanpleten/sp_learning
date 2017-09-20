from sp_at.actions.career_page_actions import CareerPageActions
from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.setup_class import fixture_webdriver
from sp_at.elements.career_page_elements import CareerPageElements
from sp_at.elements.main_page_elements import MainPageElements


def test_general_elements(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url('http://console.dev.sonikpass.com/#careers')

    # check header elements
    general_action.check_element_on_page(mp_element.logo())
    general_action.check_element_on_page(mp_element.signup_button())
    general_action.check_element_on_page(mp_element.login_button())
    general_action.check_element_on_page(mp_element.hamburger_menu_button())

    # check footer elements
    # general_action.check_element_on_page(mp_element.footer_whyus())
    # general_action.check_element_on_page(mp_element.footer_company())
    # general_action.check_element_on_page(mp_element.footer_career())
    # general_action.check_element_on_page(mp_element.footer_faq())
    # general_action.check_element_on_page(mp_element.footer_contact())


def test_career_page(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    car_action = CareerPageActions(fixture_webdriver)
    car_element = CareerPageElements(fixture_webdriver)

    general_action.open_page_by_url('http://console.dev.sonikpass.com/#careers')

    car_action.check_list_of_elements(1, 5)
    general_action.check_element_on_page(car_element.faq_button())


def test_button(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    car_element = CareerPageElements(fixture_webdriver)

    general_action.open_page_by_url('http://console.dev.sonikpass.com/#careers')
    general_action.click_on_button(car_element.faq_button())
    general_action.check_url('http://console.dev.sonikpass.com/#faq')
