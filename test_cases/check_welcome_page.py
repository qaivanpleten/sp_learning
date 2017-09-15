from actions.general_actions import GeneralActions
from actions.login_actions import LoginActions
from actions.setup_class import SetUpClass
from elements.main_page_elements import MainPageElements
from elements.welcome_page_elements import WelcomePageElements


class CheckWelcomePage(SetUpClass):
    def test_page_elements(self):
        general_action = GeneralActions(self.driver)
        mp_element = MainPageElements(self.driver)
        welcome_elements = WelcomePageElements(self.driver)
        LoginActions(self.driver).login_full_case('test@selenium.ua')

        # check elements
        general_action.check_element_on_page(mp_element.logo())
        general_action.check_element_on_page(mp_element.hamburger_menu_button())

        general_action.check_element_on_page(welcome_elements.logout_button())
        general_action.check_element_on_page(welcome_elements.welcome_time())
        general_action.check_element_on_page(welcome_elements.content_block())
        general_action.check_element_on_page(welcome_elements.dashboard_button())
        general_action.check_element_on_page(welcome_elements.partner_button())

        # # check footer elements
        # general_action.check_element_on_page(mp_element.footer_whyus())
        # general_action.check_element_on_page(mp_element.footer_company())
        # general_action.check_element_on_page(mp_element.footer_career())
        # general_action.check_element_on_page(mp_element.footer_faq())
        # general_action.check_element_on_page(mp_element.footer_contact())

