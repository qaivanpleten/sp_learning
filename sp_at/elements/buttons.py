from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.elements.element import Element, ElementByXpath


class Button(ABC):
    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def present(self) -> bool:
        pass


class ButtonOf(Button):
    def __init__(self, element: Element):

        self._button = element

    def click(self):
        self._button.instance().click()

    def present(self) -> bool:
        return self._button.instance().is_displayed()


class ButtonByXPath(Button):
    def __init__(self, driver: WebDriver, xpath: str):
        self._button = ButtonOf(ElementByXpath(driver, xpath))

    def click(self):
        self._button.click()

    def present(self) -> bool:
        return self._button.present()