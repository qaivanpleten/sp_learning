from selenium.webdriver.support.select import Select


class EditUsersPageElements:
    def __init__(self, driver):
        self.driver = driver

    def username_block(self):
        return self.driver.find_element_by_id('username')

    def username_input(self):
        return self.driver.find_element_by_xpath('//*[@id="username"]/div/input')

    def first_name_block(self):
        return self.driver.find_element_by_id('firstname')

    def first_name_input(self):
        return self.driver.find_element_by_xpath('//*[@id="firstname"]/div/input')

    def last_name_block(self):
        return self.driver.find_element_by_id('lastname')

    def last_name_input(self):
        return self.driver.find_element_by_xpath('//*[@id="lastname"]/div/input')

    def email_block(self):
        return self.driver.find_element_by_id('emails')

    def email_input(self):
        return self.driver.find_element_by_xpath('//*[@id="emails"]/div/span/form/div[1]/input')

    def phone_block(self):
        return self.driver.find_element_by_id('telephones')

    def phone_input(self):
        return self.driver.find_element_by_xpath('//*[@id="telephones"]/div/span/form/div[1]/input')

    def data_block(self):
        return self.driver.find_element_by_id('basic-data')

    def role_select(self):
        return self.driver.find_element_by_class_name('sp-select-role')

    def suspend_button(self):
        return self.driver.find_element_by_xpath('//*[@id="user-actions"]/button[1]')

    def delete_button(self):
        return self.driver.find_element_by_xpath('//*[@id="user-actions"]/button[2]')

    def activity_block(self):
        return self.driver.find_element_by_id('activity-region')

    def back_button(self):
        return self.driver.find_element_by_xpath('//*[@id="actions-panel"]/span[1]/a/span')

