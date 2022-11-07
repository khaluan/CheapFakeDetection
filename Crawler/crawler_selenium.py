from selenium import webdriver

def save_screenshot(driver: webdriver.Chrome, path: str = './Output.png') -> None:
    # Ref: https://stackoverflow.com/a/52572919/
    print("Inside function")
    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    print(required_height, required_width)
    driver.set_window_size(required_width, required_height)
    # driver.save_screenshot(path)  # has scrollbar
    driver.find_element_by_tag_name('body').screenshot(path)  # avoids scrollbar
    driver.set_window_size(original_size['width'], original_size['height'])

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get("https://www.nytimes.com/2019/01/12/us/politics/julian-castro-president-announce.html")
save_screenshot(driver)
driver.close()