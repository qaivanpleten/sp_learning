from actions.login_actions import LoginActions

from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.welcome_page_elements import WelcomePageElements


class UsersPageActions:
    def __init__(self, driver):
        self.driver = driver

    def open_users_page(self):
        LoginActions(self.driver).login_full_case('test@selenium.ua')
        GeneralActions(self.driver).click_on_button(WelcomePageElements(self.driver).dashboard_button())
