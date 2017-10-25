import allure
import pytest

from sp_at.pages.integration_page import InitialIntegrationPage


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on Integration page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page = InitialIntegrationPage(fixture_webdriver)
    page.open()
    assert page.header().present(), "Header is brocken: some element isn't displayed"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Integration page')
@allure.story('Integration page elements')
def test_page_elements(fixture_webdriver):
    page = InitialIntegrationPage(fixture_webdriver)
    page.open()
    assert page.body().present(), "Page's body is brocken: some element isn't displayed"
