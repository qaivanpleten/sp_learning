import time

from actions.general_actions import GeneralActions
from actions.setup_class import SetUpClass
from elements.install_page_elements import InstallPageElements
from elements.main_page_elements import MainPageElements


class CheckInstallPage(SetUpClass):
    def test_general_elements(self):
        general_action = GeneralActions(self.driver)
        mp_element = MainPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#install')

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
        install_element = InstallPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#install')
        time.sleep(3)

        general_action.check_element_on_page(install_element.install_title())
        general_action.check_element_on_page(install_element.install_on_ios())
        general_action.check_element_on_page(install_element.install_desktop())
        general_action.check_element_on_page(install_element.install_on_android())
        general_action.scroll_page('500')
        general_action.check_element_on_page(install_element.content_block())
        general_action.check_element_on_page(install_element.troubleshooting_title())
        general_action.check_element_on_page(install_element.troubleshooting_block())

        general_action.click_on_button(install_element.troubleshooting_button_how_do_())
        general_action.check_element_on_page(install_element.troubleshooting_text_how_do_())

        general_action.scroll_page('1100')
        time.sleep(2)
        general_action.click_on_button(install_element.troubleshooting_button_app_is())
        general_action.check_element_on_page(install_element.troubleshooting_text_how_do_())

        general_action.scroll_page('1400')
        time.sleep(2)
        general_action.click_on_button(install_element.troubleshooting_button_download())
        general_action.check_element_on_page(install_element.troubleshooting_text_download())


    def test_ios_buttons(self):
        general_action = GeneralActions(self.driver)
        install_element = InstallPageElements(self.driver)
        general_action.open_page_by_url('http://console.dev.sonikpass.com/#install')
        time.sleep(3)

        general_action.click_on_button(install_element.install_on_ios())
        general_action.check_url('https://beta.itunes.apple.com/v1/app/1140636912')


