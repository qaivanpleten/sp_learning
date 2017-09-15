class UsersPageElements:
    def __init__(self, driver):
        self.driver = driver

    def users_title(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/h1')

    def list_of_emails(self):
        return self.driver.find_element_by_id('users-holder')

    def content_left(self):
        return self.driver.find_element_by_id('content_left')

    def content_right(self):
        return self.driver.find_element_by_id('content_right')


