from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



options = Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")

service = Service(executable_path='/root/thesis/lib/chromedriver')
driver = webdriver.Chrome(options=options, service = service)
driver.get("http://google.com/")
print ("Headless Chrome Initialized")
driver.quit()
