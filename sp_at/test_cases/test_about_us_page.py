import allure
import pytest

from sp_at.pages.about_us_page import InitialAboutUsPage


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on AboutUs page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page = InitialAboutUsPage(fixture_webdriver)
    page.open()
    assert page.header().present(), "The header of Why page is broken"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on AboutUs page')
@allure.story('AboutUs page elements')
def test_aboutus_elements(fixture_webdriver):
    page = InitialAboutUsPage(fixture_webdriver)
    page.open()
    assert page.body().present(), "Body elements aren't displayed"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on AboutUs page')
@allure.story('AboutUs page buttons')
def test_buttons(fixture_webdriver):
    page = InitialAboutUsPage(fixture_webdriver)
    page.open()
    page.open_position().click()
    assert not page.body().present(), "Button isn't working. Or button doesn't redirect to corresponding page"

    # ToDo change assert when Career page will be implement
