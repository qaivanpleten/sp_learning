import allure
import pytest

from sp_at.pages.why_page import InitialWhyPage, SlowWhyPage


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on WhyUs page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page = SlowWhyPage(InitialWhyPage(fixture_webdriver))
    page.open()
    assert page.header().present(), "The header of Why page is broken"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on WhyUs page')
@allure.story('WhyUs page elements')
def test_page_elements(fixture_webdriver):
    page = InitialWhyPage(fixture_webdriver)
    page.open()
    assert page.body().present(), "The body of Why page is broken"
