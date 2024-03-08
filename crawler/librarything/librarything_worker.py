import random
import re
import time
from selenium import webdriver
from crawler.base.base_worker import BaseWorker
from crawler.support import constants
from crawler.support.items import BookItem

class LibraryThingWorker(BaseWorker):
    number_regex = r"\d+(,\d+)*"
    
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
            time.sleep(random.randint(2, 3))
            link_to_full_list = self.find_element_xpath(xpath=constants.LIBRARYTHINGS_LINK_TO_FULL_LIST_BOOK_XPATH)
            if link_to_full_list == None:
                continue
            
            time.sleep(random.randint(2, 3))
            link_to_full_list.click()
            time.sleep(random.randint(2, 3))

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
        language = self._extract_language()
        average_rating = self._extract_average_rating()
        rating_count = self._extract_rating_count()
        num_page = self._extract_num_page()

        return BookItem(name=name, description=description, genres=genres, author=author, series=series, related_people=related_people, 
                        url=url_to_book, language=language, average_rating=average_rating, rating_count=rating_count, num_page=num_page)

    def _extract_name(self) -> str:
        name = self.find_element_xpath(constants.LIBRARYTHINGS_TITLE_XPATH)
        if name == None:
            return ""
        return name.text
        
    def _extract_author(self) -> list[str]:
        authors = self.find_list_element_xpath(constants.LIBRARYTHINGS_AUTHOR_XPATH)
        result = set()

        for author in authors:
            result.add(author.text.strip())

        return list(result)
    
    def _extract_related_people(self) -> dict | None:
        related_people_name = self.find_list_element_xpath(constants.LIBRARYTHINGS_RELATED_PEOPLE_NAME_XPATH)
        if (len(related_people_name)) == 0:
            return None
        
        related_people_position = self.find_list_element_xpath(constants.LIBRARYTHINGS_RELATED_PEOPLE_POSITION_XPATH)

        result = {}
        for index in range(len(related_people_name)):
            person_name = related_people_name[index].text.strip()
            raw_person_position = related_people_position[index].text.strip()

            person_position = ''
            for char in raw_person_position:
                if (char == '(') or (char == ')'):
                    continue
                elif char == '_':
                    person_position += ' '
                else:
                    person_position += char
            
            result.update({person_name: person_position})

        return result
    
    def _extract_description(self) -> str:
        description_show_more_link = self.find_element_xpath(constants.LIBRARYTHINGS_DESCRIPTION_SHOW_MORE_LINK_XPATH)
        if description_show_more_link is None:
            description = self.find_element_xpath(constants.LIBRARYTHINGS_DESCRIPTION_XPATH)
            if description is None:
                return ""
            return description.text
        else:
            description_show_more_link.click()
            description_show_more_hide = self.find_element_xpath(constants.LIBRARYTHINGS_DESCRIPTION_SHOW_MORE_HIDE_XPATH)
            description_show_more_show = self.find_element_xpath(constants.LIBRARYTHINGS_DESCRIPTION_SHOW_MORE_SHOW_XPATH)
            return description_show_more_show.text + " " + description_show_more_hide.text
        
    def _extract_genres(self) -> list[str]:
        genre_list = self.find_list_element_xpath(constants.LIBRARYTHINGS_GENRE_LIST_XPATH)
        genres = []
        for genre in genre_list:
            genres.append(genre.text)

        return genres
    
    def _extract_series(self) -> str:
        series_num = self.find_element_xpath(constants.LIBRARYTHINGS_SERIES_NUM_XPATH)
        if series_num == None:
            return ""
        series_name = self.find_element_xpath(constants.LIBRARYTHINGS_SERIES_NAME_XPATH)
        return series_name.text + series_num.text
    
    def _extract_language(self) -> str | None:
        language_element = self.find_element_xpath(xpath=constants.LIBRARYTHINGS_BOOK_LANGUAGE)
        if language_element == None:
            return None
        
        return language_element.text.strip()

    def _extract_average_rating(self) -> float:
        avg_rating_element = self.find_element_xpath(xpath=constants.LIBRARYTHINGS_BOOK_RATING)
        if avg_rating_element is None:
            return 0.0
        
        return float(avg_rating_element.text[1:len(avg_rating_element.text.strip()) - 1])

    def _extract_rating_count(self) -> int:
        time.sleep(random.randint(2, 3))
        rating_count = 0
        rating_count_elements = self.find_list_element_xpath(constants.LIBRARYTHINGS_BOOK_RATING_COUNT)
        for rating_count_element in rating_count_elements:
            text = rating_count_element.text.strip()
            if text:
                number_within_text = int(text)
                print(number_within_text)
                rating_count += number_within_text
        return rating_count


    def _extract_num_page(self) -> int | None:
        num_page_line = self.find_element_xpath(xpath=constants.GOODREADS_BOOK_NUM_PAGE)
        if num_page_line == None:
            return None
        
        text = num_page_line.text
        return self._find_number_within_text(text=text)

    def _find_number_within_text(self, text: str) -> int | None:
        return None