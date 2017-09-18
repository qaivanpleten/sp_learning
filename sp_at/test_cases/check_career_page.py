from sp_at.actions.career_page_actions import CareerPageActions
from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.setup_class import SetUpClass
from sp_at.elements.career_page_elements import CareerPageElements
from sp_at.elements.main_page_elements import MainPageElements


class CheckCareerPage(SetUpClass):
    def test_general_elements(self):
        general_action = GeneralActions(self.driver)
        mp_element = MainPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#careers')

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

    def test_career_page(self):
        general_action = GeneralActions(self.driver)
        car_action = CareerPageActions(self.driver)
        car_element = CareerPageElements(self.driver)

        general_action.open_page_by_url('http://console.dev.sonikpass.com/#careers')

        car_action.check_list_of_elements(1, 5)
        general_action.check_element_on_page(car_element.faq_button())

    def test_button(self):
        general_action = GeneralActions(self.driver)
        car_element = CareerPageElements(self.driver)

        general_action.open_page_by_url('http://console.dev.sonikpass.com/#careers')
        general_action.click_on_button(car_element.faq_button())
        general_action.check_url('http://console.dev.sonikpass.com/#faq')
