from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.login_actions import LoginActions
from sp_at.elements.users_page_elements import UsersPageElements
from sp_at.elements.welcome_page_elements import WelcomePageElements


class UsersPageActions:
    def __init__(self, driver):
        self.driver = driver

    def open_users_page(self):
        LoginActions(self.driver).login_full_case('admin@selenium.dp')
        GeneralActions(self.driver).click_on_button(WelcomePageElements(self.driver).dashboard_button())

    def fill_new_user_form(self, firsname=None, lastname=None, email=None, country_code=None, phone=None):
        form_element = UsersPageElements(self.driver)

        GeneralActions(self.driver).click_on_button(form_element.new_user_button())
        form_element.firstname_input().send_keys(firsname)
        form_element.lastname_input().send_keys(lastname)
        form_element.email_input().send_keys(email)
        form_element.country_code_input().click()
        form_element.country_code_input().clear()
        form_element.country_code_input().send_keys(country_code)
        form_element.phone_number_input().send_keys(phone)

        GeneralActions(self.driver).click_on_button(form_element.submit_button())

