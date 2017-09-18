import time

from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.setup_class import SetUpClass
from sp_at.elements.main_page_elements import MainPageElements
from sp_at.elements.why_page_elements import WhyPageElements


class CheckWhyPage(SetUpClass):
    def test_general_elements(self):
        general_action = GeneralActions(self.driver)
        mp_element = MainPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#why')

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
        why_element = WhyPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#why')
        time.sleep(3)

        general_action.check_element_on_page(why_element.why_title())
        general_action.check_element_on_page(why_element.ten_reasons_title())
        general_action.check_element_on_page(why_element.ten_reasons_text_block())
        general_action.scroll_page('1000')
        general_action.check_element_on_page(why_element.have_question_button())
        general_action.check_element_on_page(why_element.try_it_button())
