from actions.general_actions import GeneralActions
from actions.setup_class import SetUpClass
from elements.main_page_elements import MainPageElements
from elements.pricing_elements import PricingPageElements


class CheckFaqPage(SetUpClass):
    def test_general_elements(self):
        general_action = GeneralActions(self.driver)
        mp_element = MainPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#pricing')

        # check header elements
        general_action.check_element_on_page(mp_element.logo())
        general_action.check_element_on_page(mp_element.signup_button())
        general_action.check_element_on_page(mp_element.login_button())
        general_action.check_element_on_page(mp_element.hamburger_menu_button())

        # check footer elements
        general_action.check_element_on_page(mp_element.footer_whyus())
        general_action.check_element_on_page(mp_element.footer_company())
        general_action.check_element_on_page(mp_element.footer_career())
        general_action.check_element_on_page(mp_element.footer_faq())
        general_action.check_element_on_page(mp_element.footer_contact())

    def test_elements(self):
        general_action = GeneralActions(self.driver)
        pricing_element = PricingPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#pricing')

        general_action.check_element_on_page(pricing_element.pricing_title())
        general_action.check_element_on_page(pricing_element.text())
        general_action.check_element_on_page(pricing_element.contact_button())
        general_action.check_element_on_page(pricing_element.try_button())

    def test_button(self):
        general_action = GeneralActions(self.driver)
        pricing_element = PricingPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#pricing')

        general_action.click_on_button(pricing_element.try_button())
        general_action.check_url('http://console.dev.sonikpass.com/#signup')
