from abc import ABC, abstractmethod

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.elements.buttons import Button, ButtonOf
from sp_at.elements.element import ElementByXpath, Element
from sp_at.elements.url import SimpleUrl, AddressOf
from sp_at.pages import main_url
from sp_at.pages.structures import Body, Header, MainHeader


class _MeetTheTeam:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def team(self) -> iter:
        for xpath_selector in range(3, 8):
            yield ElementByXpath(self._driver, '//*[@id="sub-region"]/div/section/div[' + str(xpath_selector) + ']')

    def present(self) -> bool:
        for member in self.team():
            if not member.instance().is_displayed():
                return False

        return True


class _Body(Body):
    def __init__(self, driver: WebDriver, open_position_button: Element):
        self._title = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div[1]/div/h1')
        self._meet_the_team_title = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div[2]/div/h1')
        self._open_positions_button = open_position_button
        self._get_in_touch_button = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div[8]/div/p/a[2]/button')
        self._team_members_blocks = _MeetTheTeam(driver)

    # elements are displayed on the page

    def present(self) -> bool:
        try:
            for elements in (
                    self._title, self._meet_the_team_title, self._open_positions_button, self._get_in_touch_button):

                if not elements.instance().is_displayed():
                    return False

            return self._team_members_blocks.present()

        except NoSuchElementException:
            return False


class AboutUsPage(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def header(self) -> Header:
        pass

    @abstractmethod
    def body(self) -> Body:
        pass

    @abstractmethod
    def open_position(self) -> Button:
        """returns instance of open_positions button"""
        pass


class InitialAboutUsPage(AboutUsPage):
    def __init__(self, driver: WebDriver):
        self._header = MainHeader(driver)
        self._browser = driver
        self._url = SimpleUrl(driver, AddressOf(main_url, '#about'))
        xpath_of_open_position_button = ElementByXpath(driver,
                                                       '//*[@id="sub-region"]/div/section/div[8]/div/p/a[1]/button')

        self._button = ButtonOf(xpath_of_open_position_button)
        self._body = _Body(driver, xpath_of_open_position_button)

    def open(self):
        self._url.open()

    def header(self) -> Header:
        return self._header

    def body(self) -> Body:
        return self._body

    def open_position(self) -> Button:
        return self._button
