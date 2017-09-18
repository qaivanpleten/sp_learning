import time

from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.login_actions import LoginActions
from sp_at.actions.setup_class import SetUpClass
from sp_at.elements.login_page_elements import LoginPageElements
from sp_at.elements.main_page_elements import MainPageElements


class CheckLoginPageElements(SetUpClass):
    def test_general_elements(self):
        general_action = GeneralActions(self.driver)
        mp_element = MainPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#login')

        # check header elements
        general_action.check_element_on_page(mp_element.logo())
        general_action.check_element_on_page(mp_element.hamburger_menu_button())

        # # check footer elements
        # general_action.check_element_on_page(mp_element.footer_whyus())
        # general_action.check_element_on_page(mp_element.footer_company())
        # general_action.check_element_on_page(mp_element.footer_career())
        # general_action.check_element_on_page(mp_element.footer_faq())
        # general_action.check_element_on_page(mp_element.footer_contact())

    def test_page_elements(self):
        general_action = GeneralActions(self.driver)
        login_element = LoginPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#login')
        time.sleep(3)

        general_action.check_element_on_page(login_element.login_page_title())
        general_action.check_element_on_page(login_element.login_form())
        general_action.check_element_on_page(login_element.account_id())
        general_action.check_element_on_page(login_element.login_input())
        general_action.check_element_on_page(login_element.login_button())
        general_action.check_element_on_page(login_element.signup_button())
        general_action.check_element_on_page(login_element.use_automatic_button())
        general_action.check_element_on_page(login_element.text_block())


class LoginCancel(SetUpClass):
    def test_cancel_login(self):
        LoginActions(self.driver).login_cancel('any@email.com')


class LoginFullTest(SetUpClass):
    def test_login(self):
        LoginActions(self.driver).login_full_case('test@selenium.ua')
        GeneralActions(self.driver).check_url("http://console.stage.sonikpass.com/#welcome")
