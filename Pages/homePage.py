from selenium.webdriver.common.by import By
from Locators.homePageLocators import HomePageLocators


class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def click_welcome(self):
        self.driver.find_element(By.XPATH, HomePageLocators.welcome_menu_xpath).click()

    def click_logut(self):
        self.driver.find_element(By.XPATH, HomePageLocators.logout_button_xpath).click()
