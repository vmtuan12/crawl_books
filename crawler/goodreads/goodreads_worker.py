from selenium import webdriver
from crawler.base.base_worker import BaseWorker
from crawler.support import constants
from crawler.support.items import BookItem

class GoodreadsWorker(BaseWorker):

    def __init__(self, target_browser: webdriver.Chrome | webdriver.Edge | webdriver.Firefox | webdriver.Safari | None):
        super().__init__(target_browser)

    def get_category_url_list(self):
        self.redirect(constants.GOODREADS_CATEGORIES_URL)
        self.load_cookies(cookie_file_path="crawler/goodreads/my_cookie_goodreads.pkl")
        self.redirect(constants.GOODREADS_CATEGORIES_URL)
        
        while (True):
            category_url_list = self.find_list_element_xpath(constants.GOODREADS_LIST_CATE_XPATH)
            
            for url in category_url_list:
                self.book_category_url_list.append(url.get_attribute("href"))

            next_page = self.find_element_xpath(constants.GOODREADS_NEXT_PAGE_CATE_XPATH)
            if next_page == None:
                break;
            
            next_page_url = next_page.get_attribute("href")
            self.redirect_after_sleep(next_page_url)

        print(self.book_category_url_list)

    def traverse_categories(self):
        for url in self.book_category_url_list:
            self.redirect_after_sleep(url)

            link_to_full_list = self.find_element_xpath(xpath=constants.GOODREADS_LINK_TO_FULL_LIST_BOOK_XPATH)
            if link_to_full_list == None:
                continue

            url = link_to_full_list.get_attribute("href")
            self.redirect_after_sleep(url)
            self.traverse_category_books()

    def traverse_category_books(self):
        while (True):
            book_list_url = self.get_book_url_list(xpath_book_list=constants.GOODREADS_LIST_BOOK_XPATH)
            for url in book_list_url:
                detail = self.extract_book_info(url_to_book=url)
                print(detail)
    

    def extract_book_info(self, url_to_book: str) -> BookItem:
        self.redirect_and_sleep(url=url_to_book)
        name = self._extract_name()
        author = self._extract_author()
        description = self._extract_description()
        genres = self._extract_genres()
        series = self._extract_series()

        return BookItem(name=name, description=description, genres=genres, author=author, series=series)

    def _extract_name(self):
        return super()._extract_name()
        
    def _extract_author(self):
        return super()._extract_author()
    
    def _extract_description(self):
        return super()._extract_description()
    
    def _extract_genres(self):
        return super()._extract_genres()
    
    def _extract_series(self):
        return super()._extract_series()