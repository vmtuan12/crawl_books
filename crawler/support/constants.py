GOODREADS_CATEGORIES_URL = "https://www.goodreads.com/genres/list"

GOODREADS_LIST_CATE_XPATH = "//*[@id='bodycontainer']//*[@class='leftContainer']//div[@class='shelfStat']//a"
GOODREADS_NEXT_PAGE_CATE_XPATH = "//a[@rel='next' and contains(text(), 'next')]"
GOODREADS_LINK_TO_FULL_LIST_BOOK_XPATH = "//a[starts-with(@href, '/shelf/show') and contains(text(), 'More')]"
GOODREADS_LIST_BOOK_XPATH = "//*[@id='bodycontainer']//a[@class='bookTitle']/parent::*/parent::*//a[starts-with(@href, '/book/show/') and @class='bookTitle']"
GOODREADS_TITLE_XPATH = "//h1"
GOODREADS_SERIES_XPATH = "//h1/preceding-sibling::h3"
GOODREADS_AUTHOR_XPATH = "//a[@class='ContributorLink']/*[text() and @data-testid='name'][not(following-sibling::*[text()])]"
GOODREADS_RELATED_PEOPLE_NAME_XPATH = "//a[@class='ContributorLink']/*[text() and @data-testid='name'][following-sibling::*[text()]]"
GOODREADS_RELATED_PEOPLE_POSITION_XPATH = "//a[@class='ContributorLink']/*[text() and @data-testid='name'][following-sibling::*[text()]]/following-sibling::*[text()]"
GOODREADS_EXPAND_AUTHOR_BTN_XPATH = "//div[@class='ContributorLinksList']//button"
GOODREADS_DESCRIPTION_XPATH = "//*[@data-testid='description']//span"
GOODREADS_EXPAND_GENRE_BTN_XPATH = "//*[@data-testid='genresList']//button"
GOODREADS_GENRE_LIST_XPATH = "//*[@data-testid='genresList']//a[contains(@href, '/genres')]"

LIBRARYTHINGS_CATEGORIES_URL = "https://www.librarything.com/genre"
LIBRARYTHINGS_LIST_CATE_XPATH = "//*[@id='classlist']/ul/li/a"
LIBRARYTHINGS_NEXT_PAGE_CATE_XPATH = "//a[contains(text(), 'next')]"
LIBRARYTHINGS_LINK_TO_FULL_LIST_BOOK_XPATH = "//a/span[contains(text(), 'Titles')]"
LIBRARYTHINGS_LIST_BOOK_XPATH = "//a[@class='popup_registered']"



