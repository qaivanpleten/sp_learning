import time

from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.main_page_elements import MainPageElements


def test_general_elements(fixture_webdriver):
    time.sleep(5)
    page_url = MainPageElements(fixture_webdriver).url()

    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)

    # check header elements
    general_action.check_element_on_page(mp_element.logo())
    general_action.check_element_on_page(mp_element.signup_button())
    general_action.check_element_on_page(mp_element.login_button())
    general_action.check_element_on_page(mp_element.hamburger_menu_button())

    # check footer elements
    general_action.check_element_on_page(mp_element.footer_whyus())
    mp_element.footer_whyus().click()
    time.sleep(3)
    general_action.check_url(page_url + '#why')
    general_action.open_page_by_url(page_url)
    time.sleep(3)

    general_action.check_element_on_page(mp_element.footer_company())
    mp_element.footer_company().click()
    time.sleep(3)
    general_action.check_url(page_url + '#about')
    general_action.open_page_by_url(page_url)
    time.sleep(3)

    general_action.check_element_on_page(mp_element.footer_career())
    mp_element.footer_career().click()
    time.sleep(3)
    general_action.check_url(page_url + '#careers')
    general_action.open_page_by_url(page_url)
    time.sleep(3)

    general_action.check_element_on_page(mp_element.footer_faq())
    mp_element.footer_faq().click()
    time.sleep(3)
    general_action.check_url(page_url + '#faq')
    general_action.open_page_by_url(page_url)
    time.sleep(3)

    general_action.check_element_on_page(mp_element.footer_contact())
    mp_element.footer_contact().click()
    time.sleep(3)
    general_action.check_url(page_url + '#contact')


def test_intro_block(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()

    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)
    time.sleep(3)
    mp_element.sidebar_intro().click()
    time.sleep(2)

    # check that Intro block is displayed
    general_action.check_active_button_in_sidebar('transform: matrix(1, 0, 0, 1, 0, 0);')

    # check block elements
    general_action.check_element_on_page(mp_element.page_title())
    general_action.check_element_on_page(mp_element.tryitnow_button())
    general_action.check_element_on_page(mp_element.howitworks_button())

    # check buttons
    mp_element.tryitnow_button().click()
    general_action.check_url(page_url + '#signup')
    general_action.open_page_by_url(page_url)
    time.sleep(2)

    mp_element.howitworks_button().click()
    time.sleep(2)
    general_action.check_active_button_in_sidebar('transform: matrix(1, 0, 0, 1, 0, -16);')


def test_problem_block(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()

    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)
    time.sleep(3)

    mp_element.sidebar_problem().click()
    time.sleep(2)

    # check that problem block is displayed
    general_action.check_active_button_in_sidebar('transform: matrix(1, 0, 0, 1, 0, -16);')

    # check block elements
    general_action.check_element_on_page(mp_element.howitworks_title())

    general_action.scroll_page('1400')
    time.sleep(2)

    general_action.check_element_on_page(mp_element.ten_reason_to_love_button())

    # check button
    mp_element.ten_reason_to_love_button().click()
    general_action.check_url(page_url + '#why')


def test_solution_block(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()

    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)
    time.sleep(3)

    mp_element.sidebar_solution().click()
    time.sleep(2)

    # check that solution block is displayed
    general_action.check_active_button_in_sidebar('transform: matrix(1, 0, 0, 1, 0, -32);')

    # check block elements
    general_action.check_element_on_page(mp_element.usability_and_security_title())

    general_action.scroll_page('2400')
    time.sleep(2)

    general_action.check_element_on_page(mp_element.faq_button())

    # check button
    mp_element.faq_button().click()
    general_action.check_url(page_url + '#faq')


def test_usages_block(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()

    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)
    time.sleep(3)

    mp_element.sidebar_usagecases().click()
    time.sleep(2)

    # check that usages block is displayed
    general_action.check_active_button_in_sidebar('transform: matrix(1, 0, 0, 1, 0, -48);')

    # check block elements
    general_action.check_element_on_page(mp_element.usability_and_security_title())

    general_action.scroll_page('5000')
    time.sleep(2)

    general_action.check_element_on_page(mp_element.slider_internet())
    mp_element.slider_right_button().click()
    time.sleep(2)
    general_action.check_element_on_page(mp_element.slider_pad())
    mp_element.slider_right_button().click()
    time.sleep(2)
    general_action.check_element_on_page(mp_element.slider_mask())
    mp_element.slider_left_button().click()
    time.sleep(2)
    general_action.check_element_on_page(mp_element.slider_pad())
    time.sleep(2)


def test_partner_block(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)
    time.sleep(3)

    mp_element.sidebar_partner().click()
    time.sleep(3)

    # check that partner block is displayed
    general_action.check_active_button_in_sidebar('transform: matrix(1, 0, 0, 1, 0, -64);')

    # check block elements
    general_action.check_element_on_page(mp_element.get_in_touch_title())
    general_action.check_element_on_page(mp_element.meet_team_button())
    general_action.check_element_on_page(mp_element.info_sonikpass_button())

    # check button
    mp_element.meet_team_button().click()
    general_action.check_url(page_url + '#about')


def test_hamburger_faq(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_faq())
    mp_element.hamburger_faq().click()
    general_action.check_url(page_url + '#faq')


def test_hamburger_about(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_about())
    mp_element.hamburger_about().click()
    general_action.check_url(page_url + '#about')


def test_hamburger_career(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_careers())
    mp_element.hamburger_careers().click()
    general_action.check_url(page_url + '#careers')


def test_hamburger_contact(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_contact())
    mp_element.hamburger_contact().click()
    general_action.check_url(page_url + '#contact')


def test_hamburger_usecases(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_usecases())
    mp_element.hamburger_usecases().click()
    general_action.check_url(page_url + '#usecases')


def test_hamburger_pricing(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_pricing())
    mp_element.hamburger_pricing().click()
    general_action.check_url(page_url + '#pricing')


def test_hamburger_integration(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_integration())
    mp_element.hamburger_integration().click()
    general_action.check_url(page_url + '#integration')


def test_hamburger_setup(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_setup())
    mp_element.hamburger_setup().click()
    general_action.check_url(page_url + '#setup')


def test_hamburger_install(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_install())
    mp_element.hamburger_install().click()
    general_action.check_url(page_url + '#install')


def test_hamburger_login(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_login())
    mp_element.hamburger_login().click()
    general_action.check_url(page_url + '#login')


def test_hamburger_signup(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_signup())
    mp_element.hamburger_signup().click()
    general_action.check_url(page_url + '#signup')


def test_hamburger_why(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_why())
    mp_element.hamburger_why().click()
    general_action.check_url(page_url + '#why')


def test_hamburger_privacy(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url)

    mp_element.hamburger_menu_button().click()
    time.sleep(3)

    general_action.check_element_on_page(mp_element.hamburger_privacy())
    mp_element.hamburger_privacy().click()
    general_action.check_url(page_url + '#privacy')
