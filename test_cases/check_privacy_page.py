import time

from actions.general_actions import GeneralActions
from actions.setup_class import SetUpClass
from elements.main_page_elements import MainPageElements
from elements.privacy_page_elemnts import PrivacyPageElements


class CheckPrivacyPage(SetUpClass):
    def test_general_elements(self):
        general_action = GeneralActions(self.driver)
        mp_element = MainPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#privacy')

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

    def test_page_elements(self):
        general_action = GeneralActions(self.driver)
        privacy_element = PrivacyPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#privacy')
        time.sleep(3)

        general_action.check_element_on_page(privacy_element.privacy_title())
        general_action.check_element_on_page(privacy_element.first_paragraph())
        general_action.check_element_on_page(privacy_element.second_paragraph())
        general_action.scroll_page('500')
        general_action.check_element_on_page(privacy_element.third_paragraph())
        general_action.check_element_on_page(privacy_element.fourth_paragraph())
        general_action.scroll_page('800')
        general_action.check_element_on_page(privacy_element.fifth_paragraph())
        general_action.scroll_page('1500')
        general_action.check_element_on_page(privacy_element.sixth_paragraph())
        general_action.check_element_on_page(privacy_element.seventh_paragraph())
        general_action.check_element_on_page(privacy_element.eighth_paragraph())
        general_action.check_element_on_page(privacy_element.questions_button())