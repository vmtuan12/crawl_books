from crawler.base.cookie_worker import CookieWorker
from crawler.goodreads.goodreads_worker import GoodreadsWorker

cookie_worker = CookieWorker()
goodreads_worker = GoodreadsWorker(target_browser=None)

if __name__ == "__main__":
    cookie_worker.get_cookies()
    for book in goodreads_worker.start_crawling():
        print(book)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")