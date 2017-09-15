import time

from actions.general_actions import GeneralActions
from actions.setup_class import SetUpClass
from elements.main_page_elements import MainPageElements
from elements.signup_page_elements import SignUpPageElements


class CheckSignUpPage(SetUpClass):
    def test_general_elements(self):
        general_action = GeneralActions(self.driver)
        mp_element = MainPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#signup')

        # check header elements
        general_action.check_element_on_page(mp_element.logo())
        general_action.check_element_on_page(mp_element.login_button())
        general_action.check_element_on_page(mp_element.hamburger_menu_button())

        # check footer elements
        # general_action.check_element_on_page(mp_element.footer_whyus())
        # general_action.check_element_on_page(mp_element.footer_company())
        # general_action.check_element_on_page(mp_element.footer_career())
        # general_action.check_element_on_page(mp_element.footer_faq())
        # general_action.check_element_on_page(mp_element.footer_contact())

    def test_page_elements(self):
        general_action = GeneralActions(self.driver)
        signup_element = SignUpPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#signup')
        time.sleep(3)

        general_action.check_element_on_page(signup_element.signup_title())
        general_action.check_element_on_page(signup_element.text_block())
        general_action.check_element_on_page(signup_element.fname_title())
        general_action.check_element_on_page(signup_element.fname_input())
        general_action.check_element_on_page(signup_element.lname_title())
        general_action.check_element_on_page(signup_element.lname_input())
        general_action.check_element_on_page(signup_element.email_title())
        general_action.check_element_on_page(signup_element.email_input())
        general_action.check_element_on_page(signup_element.phone_block())
        general_action.check_element_on_page(signup_element.country_code_input())
        general_action.check_element_on_page(signup_element.phone_input())
        general_action.check_element_on_page(signup_element.create_account_button())