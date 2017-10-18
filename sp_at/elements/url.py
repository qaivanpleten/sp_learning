from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver


class Address(ABC):
    @abstractmethod
    def value(self) -> str:
        pass


class SimpleAddress(Address):
    def __init__(self, url: str):
        self._addr = url

    def value(self) -> str:
        return self._addr


class CompositeAddress(Address):
    def __init__(self, base: str, suffix: str):
        self._base = base
        self._suffix = suffix

    def value(self) -> str:
        return self._base + self._suffix


class AddressOf(Address):
    def __init__(self, base: Address, suffix: str):
        self._suffix = suffix
        self._base = base

    def value(self) -> str:
        return CompositeAddress(self._base.value(), self._suffix).value()


class Url(ABC):
    @abstractmethod
    def open(self):
        pass


class SimpleUrl(Url):
    def __init__(self, browser: WebDriver, url: Address):
        self._browser = browser
        self._addr = url

    def open(self):
        self._browser.get(self._addr.value())
