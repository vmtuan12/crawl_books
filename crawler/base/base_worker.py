from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time
import random

class BaseWorker:

    url_list = []

    def __init__(self, target_browser: webdriver.Chrome | webdriver.Edge | webdriver.Firefox | webdriver.Safari):
        self.browser = target_browser

    def go_to(self, url: str):
        time.sleep(random.randint(3, 8))
        self.browser.get(url)

    def get_book_url_list(self, xpath_book_list: str) -> list[str]:
        result = []
        book_list = self._make_book_list(xpath=xpath_book_list)

        for book in book_list:
            result.append(book.get_attribute("href"))

        return result
    
    def extract_book_info(self, url_to_book: str) -> dict:
        pass
    
    def _make_book_list(self, xpath: str) -> list[WebElement]:
        return self.browser.find_elements(by=By.XPATH, value=xpath)