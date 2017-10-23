from selenium.webdriver.remote.webdriver import WebDriver


# class BasePage(object):
#     def __init__(self, driver: WebDriver):
#         self.driver = driver


class MainElements:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def present_header_elements(self):
        logo = self.driver.find_element_by_xpath('//*[@id="app-container"]/a/div[2]')
        signup_button = self.driver.find_element_by_id('signup_link')
        login_button = self.driver.find_element_by_xpath('//*[@id="app-container"]/div[2]/button')
        hamburger_menu_button = self.driver.find_element_by_xpath('//*[@id="app-container"]/div[1]/div')

        for elements in (logo, signup_button, login_button, hamburger_menu_button):
            if elements.is_displayed():
                return True

            else:
                return False

    def general_url(self):
        return 'http://console.sonikpass.com/'
