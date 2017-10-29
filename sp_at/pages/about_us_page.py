import time
from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.elements.element import ElementByXpath
from sp_at.elements.url import SimpleUrl, AddressOf
from sp_at.pages import main_url
from sp_at.pages.structures import Body, Header, MainHeader


class _Body(Body):
    def __init__(self, driver: WebDriver):
        self._title = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div[1]/div/h1')
        self._meet_the_team_title = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div[2]/div/h1')
        self._open_positions_button = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div[8]/div/p/a[1]/button')
        self._get_in_touch_button = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div[8]/div/p/a[2]/button')

        # xpath_selector = 3
        # self._portfolio_block = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div[' + str(xpath_selector) + ']')
        # self._portfolio_block = ElementByXpath('//*[@id="sub-region"]/div/section/div[3]')


    # elements are displayed on the page

    def present(self) -> bool:
        for elements in (
        self._title, self._meet_the_team_title, self._open_positions_button, self._get_in_touch_button):
            if not elements.instance().is_displayed():
                return False
            else:
                return True

                # while xpath_selector <= 8:
                #     xpath_selector = 3
                #     portfolio_block = self.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[' + str(xpath_selector) + ']')
                #     if portfolio_block.is_displayed():
                #         return True
                #     else:
                #         return False
                #
                #     xpath_selector += 1

                # def open_position_button_work(self):
                #     open_position_button = self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[8]/div/p/a[1]/button')
                #     open_position_button.click()
                #     time.sleep(3)
                #
                #     if MainElements.general_url(self) + '#careers' in self.driver.current_url:
                #         return True
                #     else:
                #         return False


class AboutUsPage(ABC):
    @abstractmethod
    def open(self):
        pass

    def header(self) -> Header:
        pass

    def body(self) -> Body:
        pass


class InitialAboutUsPage(AboutUsPage):
    def __init__(self, driver: WebDriver):
        self._header = MainHeader(driver)
        self._browser = driver
        self._url = SimpleUrl(driver, AddressOf(main_url, '#about'))
        self._body = _Body(driver)

    def open(self):
        self._url.open()

    def header(self) -> Header:
        return self._header

    def body(self) -> Body:
        return self._body
