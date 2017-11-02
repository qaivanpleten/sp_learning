import time
from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Element(ABC):
    @abstractmethod
    def instance(self) -> WebElement:
        """Returns a loaded WebElement"""


class ElementByXpath(Element):
    def __init__(self, driver: WebDriver, xpath: str):
        self._browser = driver
        self._locator = xpath

    def instance(self) -> WebElement:
        return self._browser.find_element_by_xpath(self._locator)


class ElementById(Element):
    def __init__(self, driver: WebDriver, id: str):
        self._browser = driver
        self._locator = id

    def instance(self) -> WebElement:
        return self._browser.find_element_by_id(self._locator)


class ElementByClassName(Element):
    def __init__(self, driver: WebDriver, class_name: str):
        self._browser = driver
        self._locator = class_name

    def instance(self) -> WebElement:
        return self._browser.find_element_by_class_name(self._locator)


class RetryOnFailure(Element):
    def __init__(self, target: Element):
        self._el = target

    def instance(self) -> WebElement:
        try:
            return self._el.instance()
        except:
            time.sleep(1)
            return self._el.instance()


