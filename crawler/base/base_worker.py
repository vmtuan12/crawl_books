from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from crawler.support.items import BookItem
import time
import random
import pickle

class BaseWorker:

    book_category_url_list = []

    def __init__(self, target_browser: webdriver.Chrome | webdriver.Edge | webdriver.Firefox | webdriver.Safari | None):
        self.browser = target_browser if target_browser != None else webdriver.Chrome()

    def start_crawling(self):
        self.get_category_url_list()
        for book in self.traverse_categories():
            yield book

    def get_category_url_list(self):
        pass

    def traverse_categories(self):
        pass

    def traverse_category_books(self):
        pass

    def load_cookies(self, cookie_file_path: str):
        cookies = pickle.load(open(cookie_file_path, "rb"))
        for cookie in cookies:
            self.browser.add_cookie(cookie)

    def redirect_and_sleep(self, url: str):
        time.sleep(random.randint(5, 8))
        self.browser.get(url)
        time.sleep(random.randint(3, 5))

    def redirect_before_sleep(self, url: str):
        self.browser.get(url)
        time.sleep(random.randint(5, 8))

    def redirect_after_sleep(self, url: str):
        time.sleep(random.randint(5, 8))
        self.browser.get(url)

    def redirect(self, url: str):
        self.browser.get(url)

    def get_book_url_list(self, xpath_book_list: str) -> list[str]:
        result = []
        book_list = self.find_list_element_xpath(xpath=xpath_book_list)

        for book in book_list:
            result.append(book.get_attribute("href"))

        return result
    
    def extract_book_info(self, url_to_book: str) -> BookItem:
        pass

    def _extract_name(self) -> str:
        pass

    def _extract_description(self) -> str:
        pass

    def _extract_author(self) -> list[str]:
        pass

    def _extract_genres(self) -> list[str]:
        pass

    def _extract_series(self) -> str | None:
        pass
    
    def find_list_element_xpath(self, xpath: str) -> list[WebElement]:
        return self.browser.find_elements(by=By.XPATH, value=xpath)
    
    def find_element_xpath(self, xpath: str) -> WebElement | None:
        try:
            result = self.browser.find_element(by=By.XPATH, value=xpath)
            return result
        except NoSuchElementException:
            return None
    
    def find_element_id(self, id: str) -> WebElement | None:
        try:
            result = self.browser.find_element(by=By.ID, value=id)
            return result
        except NoSuchElementException:
            return None