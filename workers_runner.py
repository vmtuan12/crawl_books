from crawler.base.cookie_worker import CookieWorker
from crawler.goodreads.goodreads_worker import GoodreadsWorker
from pipeline import pipeline, topic

cookie_worker = CookieWorker()
goodreads_worker = GoodreadsWorker(target_browser=None)

kafka_connector = pipeline.KafkaConnector()

if __name__ == "__main__":
    # cookie_worker.get_cookies()
    for book in goodreads_worker.start_crawling():
        kafka_connector.send(msg=book)
        print(book)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    kafka_connector.close()