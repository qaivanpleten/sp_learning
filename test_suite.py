import unittest

from test_cases.check_about_us_page import CheckAboutUsPage
from test_cases.check_career_page import CheckCareerPage
from test_cases.check_contact_us import CheckContactUsPage
from test_cases.check_faq_page import CheckFaqPage
from test_cases.check_integration_page import CheckIntegrationPage
from test_cases.check_main_page import CheckMainPageElements, CheckHamburgerMenu
from test_cases.check_pricing_page import CheckPricingPage
from test_cases.check_setup_page import CheckSetupPage

main_page_elements = unittest.TestLoader().loadTestsFromTestCase(CheckMainPageElements)
main_page_hamburger = unittest.TestLoader().loadTestsFromTestCase(CheckHamburgerMenu)
about_us_page = unittest.TestLoader().loadTestsFromTestCase(CheckAboutUsPage)
career_page = unittest.TestLoader().loadTestsFromTestCase(CheckCareerPage)
contact_us_page = unittest.TestLoader().loadTestsFromTestCase(CheckContactUsPage)
faq_page = unittest.TestLoader().loadTestsFromTestCase(CheckFaqPage)
integration_page = unittest.TestLoader().loadTestsFromTestCase(CheckIntegrationPage)
pricing_page = unittest.TestLoader().loadTestsFromTestCase(CheckPricingPage)
setup_page = unittest.TestLoader().loadTestsFromTestCase(CheckSetupPage)

smoke_test = unittest.TestSuite((main_page_elements, main_page_hamburger, about_us_page, career_page, contact_us_page,
                                faq_page, integration_page, pricing_page, setup_page))

unittest.TextTestRunner(verbosity=2).run(smoke_test)