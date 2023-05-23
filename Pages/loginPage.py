from selenium.webdriver.common.by import By
from Locators.loginPageLocators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, LoginPageLocators.username_textbox_name).clear()
        self.driver.find_element(By.NAME, LoginPageLocators.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, LoginPageLocators.password_textbox_name).clear()
        self.driver.find_element(By.NAME, LoginPageLocators.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, LoginPageLocators.login_button_xpath).click()

    def check_invalid_username_message(self):
        message = self.driver.find_element(By.XPATH, LoginPageLocators.invalid_cred_xpath)
        return message
