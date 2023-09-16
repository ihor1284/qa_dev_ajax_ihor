from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

class Page:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, by: MobileBy = MobileBy.ID, link: str = None) -> WebElement:
        """
        Find and return a web element using the specified 'by' and 'link' arguments.
        Waits until the element is present before returning it.
        """
        return self.wait.until(EC.presence_of_element_located((by, link)))
    
    def find_elements(self, by: MobileBy, link: str = None) -> WebElement:
        """
        Find and return a list of WebElements located by the given strategy and link text.
        
        Args:
            by (MobileBy): The strategy used to locate the elements.
            link (str, optional): The link text of the elements to be located.
        
        Returns:
            WebElement: A list of WebElements located by the given strategy and link text.
        """
        elements = self.wait.until(EC.presence_of_all_elements_located((by, link)))
        return elements

    def click_element(self, by: MobileBy = MobileBy.ID, link: str = None) -> None:
        """
        Clicks on an element identified by the given locator.

        Args:
            by (MobileBy, optional): The locator strategy to use. Defaults to MobileBy.ID.
            link (str, optional): The identifier of the element. Defaults to None.

        Returns:
            None: This function does not return anything.
        """
        self.find_element(by, link).click()

    def send_keys(self, by: MobileBy, link: str = None, *args) -> None:
        """
        Sends keys to a mobile element using the specified locator and optional link text.

        :param by: The locator strategy to use for finding the element.
        :param link: The optional link text to use for finding the element.
        :param args: The keys to send to the element.
        :return: None
        """
        if len(args) > 1:
            elements = self.find_elements(by, link)
            for index, element in enumerate(elements):
                element.send_keys(args[index])
                sleep(2) #Sleep to avoid login ban
        else:
            element = self.find_element(by, link)
            element.send_keys(*args)
