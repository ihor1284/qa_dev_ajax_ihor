from .page import Page
from utils.elements import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class LoginPage(Page):
    def login(self, email: str, password: str) -> bool:
        """
        Logs in the user with the given email and password.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the login is successful, False otherwise.
        """
        self.click_element(link=AUTH_BTN)
        self.send_keys(MobileBy.CLASS_NAME, CREDS_CLASS, email, password)
        self.click_element(link=LOGIN_BTN)
        try:
            self.find_element(link=MENU)
            return True
        except (NoSuchElementException, TimeoutException):
            self.click_element(link=BACK)
            return False