from actions.setup_class import SetUpClass
from actions.users_page_actions import UsersPageActions


class CheckUsersPageElements(SetUpClass):
    def test_check_elements(self):
        UsersPageActions(self.driver).open_users_page()
    