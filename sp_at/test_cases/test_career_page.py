import time

import allure
import pytest

from sp_at.pages.career_page import InitialCareerPage


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on Career page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page = InitialCareerPage(fixture_webdriver)
    page.open()
    assert page.header().present(), "The header of Career page is broken"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Career page')
@allure.story('Career page elements')
def test_career_page(fixture_webdriver):
    page = InitialCareerPage(fixture_webdriver)
    page.open()
    assert page.body().present(), "Some elements in page body isn't presented"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Career page')
@allure.story('Career page buttons')
def test_button(fixture_webdriver):
    page = InitialCareerPage(fixture_webdriver)
    page.open()
    page.faq_button().click()
    time.sleep(5)
    assert not page.body().present(), "Button isn't working"

    # TODO change assert when FAQ page will be implemented
