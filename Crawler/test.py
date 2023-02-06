post = {'post_url': 'https://www.nytimes.com/2019/06/13/us/politics/julian-castro-fox-town-hall.html', 'title': "Highlights From Julián Castro's Fox News Town Hall", 'lang': 'en'}
url = post['post_url']

from selenium_crawler import sel
from crawler import parse_content
import request_crawler as req
print('Crawling....')
content = req.get_content(post)
print("Crawl complete")
print("Extracting.....")
print(parse_content(content, post))

