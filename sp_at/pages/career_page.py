from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.elements.buttons import Button, ButtonOf
from sp_at.elements.element import ElementByXpath
from sp_at.elements.url import SimpleUrl, AddressOf
from sp_at.pages import main_url
from sp_at.pages.structures import Body, Header, MainHeader


class _Body(Body):
    def __init__(self, driver: WebDriver):
        self._career_title = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div/div/h1')
        self._open_position_title = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div/div/p[4]/strong')
        self._faq_button = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div/div/p[6]/a[1]/button')
        self._get_in_touch_button = ElementByXpath(driver, '//*[@id="sub-region"]/div/section/div/div/p[6]/a[2]/button')

    def present(self) -> bool:
        for element in (self._career_title, self._faq_button, self._open_position_title, self._get_in_touch_button):
            if not element.instance().is_displayed():
                return False
        return True


class CareerPage(ABC):
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
    def faq_button(self) -> Button:
        pass


class InitialCareerPage(CareerPage):
    def __init__(self, driver: WebDriver):
        self._header = MainHeader(driver)
        self._browser = driver
        self._url = SimpleUrl(driver, AddressOf(main_url, "#careers"))
        self._faq_button = ButtonOf(_Body(driver)._faq_button)
        self._body = _Body(driver)

    def open(self):
        self._url.open()

    def header(self) -> Header:
        return self._header

    def body(self) -> Body:
        return self._body

    def faq_button(self) -> Button:
        return self._faq_button
