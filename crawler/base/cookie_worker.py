from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pickle

class CookieWorker:
    def get_cookies(self):
        self._get_cookie_goodreads()

    def _get_cookie_goodreads(self):
        browser = webdriver.Chrome()

        browser.get("https://www.goodreads.com/ap/signin?openid.return_to=https%3A%2F%2Fwww.goodreads.com%2Fap-handler%2Fregister&prevRID=K21HZM54ZPA91Z5VA076&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_goodreads_web_na&openid.mode=checkid_setup&siteState=68ffc395c0c554224dd4fd1f413f10b4&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_goodreads_web_na&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        user_field = browser.find_element(by="id", value="ap_email")
        user_field.send_keys("minhtuan3154@gmail.com")

        password_field = browser.find_element(by="id", value="ap_password")
        password_field.send_keys("Tuan$281203")
        password_field.send_keys(Keys.ENTER)

        sleep(10)

        pickle.dump(browser.get_cookies(), open("crawler/goodreads/my_cookie_goodreads.pkl", "wb"))