from actions.general_actions import GeneralActions
from actions.setup_class import SetUpClass
from elements.integration_page_elements import IntegrationPageElements
from elements.main_page_elements import MainPageElements


class CheckIntegrationPage(SetUpClass):
    def test_general_elements(self):
        general_action = GeneralActions(self.driver)
        mp_element = MainPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#integration')

        # check header elements
        general_action.check_element_on_page(mp_element.logo())
        general_action.check_element_on_page(mp_element.signup_button())
        general_action.check_element_on_page(mp_element.login_button())
        general_action.check_element_on_page(mp_element.hamburger_menu_button())

        # # check footer elements
        # general_action.check_element_on_page(mp_element.footer_whyus())
        # general_action.check_element_on_page(mp_element.footer_company())
        # general_action.check_element_on_page(mp_element.footer_career())
        # general_action.check_element_on_page(mp_element.footer_faq())
        # general_action.check_element_on_page(mp_element.footer_contact())

    def test_page_elements(self):
        general_action = GeneralActions(self.driver)
        int_element = IntegrationPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#integration')

        general_action.check_element_on_page(int_element.integration_title())
        general_action.check_element_on_page(int_element.schedule_block())
        general_action.check_element_on_page(int_element.what_next_block())
        general_action.check_element_on_page(int_element.schedule_button())