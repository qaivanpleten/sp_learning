import time

from sp_at.elements.edit_user_page_elements import EditUsersPageElements
from sp_at.elements.users_page_elements import UsersPageElements
from selenium import webdriver
from selenium.webdriver.support.select import Select as WebDriverSelect


class EditUsersPageActions:
    def __init__(self, driver):
        self.driver = driver

    def delete_user(self):
        EditUsersPageElements(self.driver).delete_button().click()
        UsersPageElements(self.driver).confirm_delete_button().click()
        time.sleep(5)

    def cancel_deleting_user(self):
        EditUsersPageElements(self.driver).delete_button().click()
        UsersPageElements(self.driver).cancel_delete_button().click()
        time.sleep(1)
        EditUsersPageElements(self.driver).back_button().click()

    def suspend_user(self):
        EditUsersPageElements(self.driver).suspend_button().click()
        time.sleep(3)

    def change_username(self, name):
        username = EditUsersPageElements(self.driver).username_input()
        username.click()
        username.clear()
        username.send_keys(name)

        EditUsersPageElements(self.driver).back_button().click()

    def change_role(self):
        dropdown = EditUsersPageElements(self.driver).role_select()
        select_list = WebDriverSelect(dropdown)
        select_list.select_by_value('0')
        selected_option = select_list.first_selected_option.text
        assert selected_option == 'admin', "Selected option should be Admin"
