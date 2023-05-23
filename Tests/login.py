import HtmlTestRunner
import sys
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = Options()
        # uncommnet fot silent-mode
        cls.options.add_argument("--headless")
        cls.options.add_argument("start-maximized")
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=cls.options)
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        homePage = HomePage(driver)
        homePage.click_welcome()
        homePage.click_logut()

        time.sleep(2)

    def test_login_invalid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username('qwerty')
        login.enter_password('admin123')
        login.click_login()
        invalid_message = login.check_invalid_username_message().text
        self.assertEqual(invalid_message, 'Invalid credentials')

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='/Users/levglukhikh/PycharmProjects/Unittest_SamplePOM/Reports'))
