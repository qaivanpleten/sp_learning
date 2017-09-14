import unittest

from test_cases.check_about_us_page import CheckAboutUsPage
from test_cases.check_career_page import CheckCareerPage
from test_cases.check_contact_us import CheckContactUsPage
from test_cases.check_faq_page import CheckFaqPage
from test_cases.check_install_page import CheckInstallPage
from test_cases.check_integration_page import CheckIntegrationPage
from test_cases.check_login_page import CheckLoginPageElements
from test_cases.check_main_page import CheckMainPageElements, CheckHamburgerMenu
from test_cases.check_pricing_page import CheckPricingPage
from test_cases.check_privacy_page import CheckPrivacyPage
from test_cases.check_setup_page import CheckSetupPage
from test_cases.check_signup_page import CheckSignUpPage

main_page_elements = unittest.TestLoader().loadTestsFromTestCase(CheckMainPageElements)
main_page_hamburger = unittest.TestLoader().loadTestsFromTestCase(CheckHamburgerMenu)
about_us_page = unittest.TestLoader().loadTestsFromTestCase(CheckAboutUsPage)
career_page = unittest.TestLoader().loadTestsFromTestCase(CheckCareerPage)
contact_us_page = unittest.TestLoader().loadTestsFromTestCase(CheckContactUsPage)
faq_page = unittest.TestLoader().loadTestsFromTestCase(CheckFaqPage)
integration_page = unittest.TestLoader().loadTestsFromTestCase(CheckIntegrationPage)
pricing_page = unittest.TestLoader().loadTestsFromTestCase(CheckPricingPage)
setup_page = unittest.TestLoader().loadTestsFromTestCase(CheckSetupPage)
install_page = unittest.TestLoader().loadTestsFromTestCase(CheckInstallPage)
login_page = unittest.TestLoader().loadTestsFromTestCase(CheckLoginPageElements)
signup_page = unittest.TestLoader().loadTestsFromTestCase(CheckSignUpPage)
privacy_page = unittest.TestLoader().loadTestsFromTestCase(CheckPrivacyPage)

smoke_test = unittest.TestSuite((main_page_elements, main_page_hamburger, about_us_page, career_page, contact_us_page,
                                faq_page, integration_page, pricing_page, setup_page, install_page, login_page,
                                 signup_page, privacy_page))

unittest.TextTestRunner(verbosity=2).run(smoke_test)