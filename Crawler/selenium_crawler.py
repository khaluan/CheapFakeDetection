from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import time


class SeleniumCrawler():
    def __init__(self) -> None:
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--enable-javascript")
        options.add_argument("--no-sandbox")
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0')
        options.add_argument('log-level=3')

        # service = Service(executable_path='/root/thesis/lib/chromedriver')
        # self.driver = webdriver.Chrome(options=options, service = service)
        self.driver = webdriver.Chrome(options = options)


    def get_content(self, post) -> str:
        url = post['post_url']
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(lambda x: self.finish_loading())
        return self.driver.page_source

    def finish_loading(self) -> bool:
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def __del__(self):
        self.driver.quit()

sel = SeleniumCrawler()
# print(sel.get_content({'post_url': 'https://www.google.com'}))
