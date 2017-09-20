from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.contact_us_page_elements import ContactPageElements
from sp_at.elements.main_page_elements import MainPageElements
from sp_at.actions.setup_class import fixture_webdriver


def test_general_elements(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url('http://console.dev.sonikpass.com/#contact')

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


def test_page_element(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    contact_element = ContactPageElements(fixture_webdriver)
    general_action.open_page_by_url('http://console.dev.sonikpass.com/#contact')

    general_action.check_element_on_page(contact_element.contact_title())
    general_action.check_element_on_page(contact_element.partnership_email())
    general_action.check_element_on_page(contact_element.support_email())
    general_action.check_element_on_page(contact_element.sales_email())
    general_action.check_element_on_page(contact_element.general_email())
    general_action.check_element_on_page(contact_element.try_it_button())
    general_action.check_element_on_page(contact_element.faq_button())


def test_button(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    contact_element = ContactPageElements(fixture_webdriver)

    general_action.open_page_by_url('http://console.dev.sonikpass.com/#contact')
    general_action.click_on_button(contact_element.faq_button())
    general_action.check_url('http://console.dev.sonikpass.com/#faq')

    general_action.open_page_by_url('http://console.dev.sonikpass.com/#contact')
    general_action.click_on_button(contact_element.try_it_button())
    general_action.check_url('http://console.dev.sonikpass.com/#signup')
