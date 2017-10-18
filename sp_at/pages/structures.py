from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.elements.element import ElementByXpath, ElementById


class Presentable(ABC):
    @abstractmethod
    def present(self) -> bool:
        pass


class Body(Presentable):
    @abstractmethod
    def present(self) -> bool:
        pass


class Header(Presentable):
    @abstractmethod
    def present(self) -> bool:
        pass


class MainHeader(Header):
    def __init__(self, driver: WebDriver):
        self._logo = ElementByXpath(driver, '//*[@id="app-container"]/a/div[2]')
        self._signup_button = ElementById(driver, 'signup_link')
        self._login_button = ElementByXpath(driver, '//*[@id="app-container"]/div[2]/button')
        self._hamburger_menu_button = ElementByXpath(driver, '//*[@id="app-container"]/div[1]/div')

    def present(self) -> bool:
        """
        Check is the header present or not.

        Returns:
            bool: True if it's present, otherwise False.
        """
        for element in (self._logo, self._signup_button, self._login_button, self._hamburger_menu_button):
            if not element.instance().is_displayed():
                return False
        return True
