import time
from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.pages.main_elements import MainElements


class BasePage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver


class AboutUsPage(BasePage):
    def open(self):
        self.get(MainElements.general_url(self) + '#about')
        assert MainElements.general_url(self) + '#about' in self.current_url

    def present_body_elements(self):
        xpath_selector = 3
        title = self.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[1]/div/h1')
        meet_the_team_title = self.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[2]/div/h1')
        #portfolio_block = self.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[' + xpath_selector + ']')
        #portfolio_block = self.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[5]')
        open_positions_button = self.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[8]/div/p/a[1]/button')
        get_in_touch_button = self.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[8]/div/p/a[2]/button')

        for elements in (title, meet_the_team_title, open_positions_button, get_in_touch_button):
            if elements.is_displayed():
                return True
            else:
                return False


        # while xpath_selector <= 8:
        #     xpath_selector = 3
        #     portfolio_block = self.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[' + str(xpath_selector) + ']')
        #     if portfolio_block.is_displayed():
        #         return True
        #     else:
        #         return False
        #
        #     xpath_selector += 1




    def open_position_button_work(self):
        open_position_button = self.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[8]/div/p/a[1]/button')
        open_position_button.click()
        time.sleep(3)

        if MainElements.general_url(self) + '#careers' in self.current_url:
            return True
        else:
            return False


