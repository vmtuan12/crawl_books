from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pickle

browser = webdriver.Chrome()

browser.get("https://www.goodreads.com/genres")

cookies = pickle.load(open("my_cookie_goodreads.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)
    
browser.get("https://www.goodreads.com/shelf/show/thriller")

result = []

book_list = browser.find_elements(by=By.XPATH, value="//*[@id='bodycontainer']//a[@class='bookTitle']/parent::*/parent::*//a[starts-with(@href, '/book/show/') and @title]")

url_list = []

for index, book in enumerate(book_list):
    url_list.append(book.get_attribute("href"))

for index, book in enumerate(url_list):
    browser.get(book)
    # time.sleep(5)
    
    title = browser.find_element(by=By.XPATH, value="//h1").text
    author = browser.find_element(by=By.XPATH, value="//a[@class='ContributorLink']/*[text()]").text
    description = browser.find_element(by=By.XPATH, value="//*[@data-testid='description']//span").text
    
    expand_genre_button = browser.find_element(by=By.XPATH, value="//*[@data-testid='genresList']//button")
    if expand_genre_button != None:
        expand_genre_button.click()

    genre_list = browser.find_elements(by=By.XPATH, value="//*[@data-testid='genresList']//a[contains(@href, '/genres')]")
    genres = []
    for genre in genre_list:
        genres.append(genre.text)

    result.append({
        "title": title,
        "author": author,
        "description": description,
        "genres": genres
    })
    # print(result)

print(result)
# page_2_btn.send_keys(Keys.)