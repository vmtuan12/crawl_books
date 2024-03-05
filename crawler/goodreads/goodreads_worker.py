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
                break
            
            next_page_url = next_page.get_attribute("href")
            self.redirect_after_sleep(next_page_url)

    def traverse_categories(self):
        for url in self.book_category_url_list:
            self.redirect_after_sleep(url)

            link_to_full_list = self.find_element_xpath(xpath=constants.GOODREADS_LINK_TO_FULL_LIST_BOOK_XPATH)
            if link_to_full_list == None:
                continue

            url = link_to_full_list.get_attribute("href")
            self.redirect_after_sleep(url)
            for book in self.traverse_category_books():
                yield book

    def traverse_category_books(self):
        while (True):
            book_list_url = self.get_book_url_list(xpath_book_list=constants.GOODREADS_LIST_BOOK_XPATH)
            if len(book_list_url) == 0:
                break

            for url in book_list_url:
                detail = self.extract_book_info(url_to_book=url)
                yield detail.to_json()

            next_page = self.find_element_xpath(xpath=constants.GOODREADS_NEXT_PAGE_CATE_XPATH)
            if next_page == None:
                break

            next_page_url = next_page.get_attribute("href")
            self.redirect_after_sleep(next_page_url)

    def extract_book_info(self, url_to_book: str) -> BookItem:
        self.redirect_and_sleep(url=url_to_book)
        name = self._extract_name()
        author = self._extract_author()
        description = self._extract_description()
        genres = self._extract_genres()
        series = self._extract_series()

        return BookItem(name=name, description=description, genres=genres, author=author, series=series)

    def _extract_name(self) -> str:
        name = self.find_element_xpath(constants.GOODREADS_TITLE_XPATH)
        if name == None:
            return ""
        return name.text
        
    def _extract_author(self) -> list[str]:
        authors = self.find_list_element_xpath(constants.GOODREADS_AUTHOR_XPATH)
        result = set()

        for author in authors:
            result.add(author.text.strip())

        return list(result)
    
    def _extract_description(self) -> str:
        description = self.find_element_xpath(constants.GOODREADS_TITLE_XPATH)
        if description == None:
            return ""
        return description.get_attribute("innerText")
    
    def _extract_genres(self) -> list[str]:
        expand_genre_button = self.find_element_xpath(constants.GOODREADS_EXPAND_GENRE_BTN_XPATH)
        if expand_genre_button != None:
            expand_genre_button.click()

        genre_list = self.find_element_xpath(constants.GOODREADS_GENRE_LIST_XPATH)
        genres = []
        for genre in genre_list:
            genres.append(genre.text)

        return genres
    
    def _extract_series(self) -> str:
        series = self.find_element_xpath(constants.GOODREADS_SERIES_XPATH)
        if series == None:
            return ""
        return series.text