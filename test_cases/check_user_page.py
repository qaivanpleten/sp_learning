import time

from actions.general_actions import GeneralActions
from actions.setup_class import SetUpClass
from actions.users_page_actions import UsersPageActions
from elements.users_page_elements import UsersPageElements


class CheckUsersPageElements(SetUpClass):
    def test_check_elements(self):
        users_element = UsersPageElements(self.driver)
        general_actions = GeneralActions(self.driver)

        UsersPageActions(self.driver).open_users_page()
        time.sleep(10)

        general_actions.check_url("http://console.stage.sonikpass.com/#users")
        general_actions.check_element_on_page(users_element.users_title())
        general_actions.check_element_on_page(users_element.list_of_emails())
        general_actions.check_element_on_page(users_element.content_left())
        general_actions.check_element_on_page(users_element.content_right())




