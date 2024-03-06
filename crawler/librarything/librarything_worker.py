import random
import time
from selenium import webdriver
from crawler.base.base_worker import BaseWorker
from crawler.support import constants
from crawler.support.items import BookItem

class LibraryThingWorker(BaseWorker):
    def __init__(self, target_browser: webdriver.Chrome | webdriver.Edge | webdriver.Firefox | webdriver.Safari | None):
        super().__init__(target_browser)
        
    def get_category_url_list(self):
        self.redirect(constants.LIBRARYTHINGS_CATEGORIES_URL)

        category_url_list = self.find_list_element_xpath(constants.LIBRARYTHINGS_LIST_CATE_XPATH)
            
        for url in category_url_list:
            self.book_category_url_list.append(url.get_attribute("href"))
            
    def traverse_categories(self):
        for url in self.book_category_url_list:
            self.redirect_after_sleep(url)
            time.sleep(random.randint(1, 2))
            link_to_full_list = self.find_element_xpath(xpath=constants.LIBRARYTHINGS_LINK_TO_FULL_LIST_BOOK_XPATH)
            if link_to_full_list == None:
                continue
            
            time.sleep(random.randint(1, 2))
            link_to_full_list.click()
            time.sleep(random.randint(1, 2))

            for book in self.traverse_category_books():
                yield book
                
    def traverse_category_books(self):
        while (True):
            book_list_url = self.get_book_url_list(xpath_book_list=constants.LIBRARYTHINGS_LIST_BOOK_XPATH)

            next_page = self.find_element_xpath(xpath=constants.LIBRARYTHINGS_NEXT_PAGE_CATE_XPATH)
            next_page_url = next_page.get_attribute("href") if next_page != None else None

            if len(book_list_url) == 0:
                break

            for url in book_list_url:
                detail = self.extract_book_info(url_to_book=url)
                yield detail.to_json()

            if next_page_url == None:
                break

            self.redirect_after_sleep(next_page_url)
            
    def extract_book_info(self, url_to_book: str) -> BookItem:
        self.redirect_and_sleep(url=url_to_book)
        name = self._extract_name()
        author = self._extract_author()
        related_people = self._extract_related_people()
        description = self._extract_description()
        genres = self._extract_genres()
        series = self._extract_series()

        return BookItem(name=name, description=description, genres=genres, author=author, series=series, related_people=related_people, url=url_to_book)