from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.setup_class import SetUpClass
from sp_at.elements.faq_page_elements import FaqPageElements
from sp_at.elements.main_page_elements import MainPageElements


class CheckFaqPage(SetUpClass):
    def test_general_elements(self):
        general_action = GeneralActions(self.driver)
        mp_element = MainPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#faq')

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

    def test_page_element(self):
        general_action = GeneralActions(self.driver)
        f_element = FaqPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#faq')

        general_action.check_element_on_page(f_element.faq_page_title())
        general_action.check_element_on_page(f_element.technology_title())
        general_action.scroll_page('320')
        general_action.check_element_on_page(f_element.technology_text_block())

        general_action.scroll_page('1050')
        general_action.check_element_on_page(f_element.troubleshooting_title())
        general_action.check_element_on_page(f_element.troubleshooting_text_block())

        general_action.scroll_page('1800')
        general_action.check_element_on_page(f_element.have_question_button())
        general_action.check_element_on_page(f_element.try_it_now_button())

    def test_buttons(self):
        general_action = GeneralActions(self.driver)
        f_element = FaqPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#faq')

        general_action.scroll_page('1800')
        general_action.click_on_button(f_element.try_it_now_button())

        general_action.check_url('http://console.dev.sonikpass.com/#signup')
