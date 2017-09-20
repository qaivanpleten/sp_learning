import time

from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.setup_class import fixture_webdriver
from sp_at.elements.main_page_elements import MainPageElements
from sp_at.elements.pricing_page_elements import PricingPageElements


def test_general_elements(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url('http://console.dev.sonikpass.com/#pricing')
    time.sleep(3)

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


def test_elements(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    pricing_element = PricingPageElements(fixture_webdriver)
    general_action.open_page_by_url('http://console.dev.sonikpass.com/#pricing')

    general_action.check_element_on_page(pricing_element.pricing_title())
    general_action.check_element_on_page(pricing_element.text())
    general_action.check_element_on_page(pricing_element.contact_button())
    general_action.check_element_on_page(pricing_element.try_button())


def test_button(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    pricing_element = PricingPageElements(fixture_webdriver)
    general_action.open_page_by_url('http://console.dev.sonikpass.com/#pricing')

    general_action.click_on_button(pricing_element.try_button())
    general_action.check_url('http://console.dev.sonikpass.com/#signup')
