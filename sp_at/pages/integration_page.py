from abc import ABC, abstractmethod

import time
from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.elements.element import ElementByXpath, ElementById
from sp_at.elements.url import SimpleUrl, AddressOf
from sp_at.pages import main_url
from sp_at.pages.structures import Body, Header, MainHeader


class _Body(Body):
    def __init__(self, driver: WebDriver):
        self._title = ElementByXpath(driver, '//*[@id="content_left"]/h1')
        self._what_next_block = ElementById(driver, 'content_right')
        self._schedule_block = ElementById(driver, 'content_left')
        self._schedule_button = ElementByXpath(driver, '//*[@id="content_right"]/a/button')

    def present(self)-> bool:
        for element in (self._title, self._what_next_block, self._schedule_block, self._schedule_button):
            if element.instance().is_displayed():
                return True
            else:
                return False


class IntegrationPage(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def header(self) -> Header:
        pass

    @abstractmethod
    def body(self) -> Body:
        pass


class InitialIntegrationPage(IntegrationPage):
    def __init__(self, driver: WebDriver):
        self._header = MainHeader(driver)
        self._browser = driver
        self._url = SimpleUrl(driver, AddressOf(main_url, '#integration'))
        self._body = _Body(driver)

    def open(self):
        self._url.open()

    def header(self) -> Header:
        return self._header

    def body(self) -> Body:
        return self._body


class SlowIntegrationPage(IntegrationPage):
    def __init__(self, page: IntegrationPage):
        self._page = page

    def open(self):
        self._page.open()
        time.sleep(5)

    def body(self) -> Body:
        time.sleep(3)
        return self._page.body()

    def header(self) -> Header:
        time.sleep(3)
        return self._page.header()

