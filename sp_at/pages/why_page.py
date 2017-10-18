import time
from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.elements.element import ElementByXpath, ElementByClassName, RetryOnFailure
from sp_at.elements.url import SimpleUrl, AddressOf
from sp_at.pages import main_url
from sp_at.pages.structures import Header, MainHeader, Body


class _Body(Body):
    def __init__(self, driver: WebDriver):
        self._title = ElementByXpath(driver, '//*[@id="flex_center"]/span/p[1]')
        self._reasons_title = RetryOnFailure(ElementByXpath(driver, '//*[@id="flex_center"]/span/h1'))
        self._reasons_text = ElementByXpath(driver, '//*[@id="flex_center"]/span/ol')
        self._question = ElementByClassName(driver, 'transparent-btn')
        self._it = ElementByClassName(driver, 'gradient-btn')

    def present(self) -> bool:
        for element in (self._title, self._reasons_title, self._reasons_text, self._question, self._it):
            if not element.instance().is_displayed():
                return False
        return True


class WhyPage(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def header(self) -> Header:
        pass

    @abstractmethod
    def body(self) -> Body:
        pass


class InitialWhyPage(WhyPage):
    def __init__(self, driver: WebDriver):
        self._header = MainHeader(driver)
        self._browser = driver
        self._url = SimpleUrl(driver, AddressOf(main_url, '#why'))
        self._body = _Body(driver)

    def open(self):
        self._url.open()

    def header(self) -> Header:
        return self._header

    def body(self) -> Body:
        return self._body


class SlowWhyPage(WhyPage):
    def __init__(self, page: WhyPage):
        self._page = page

    def open(self):
        self._page.open()
        time.sleep(3)

    def body(self) -> Body:
        time.sleep(2)
        return self._page.body()

    def header(self) -> Header:
        time.sleep(2)
        return self._page.header()
