from util import request
from bs4 import BeautifulSoup
import logging
from preprocess import relevant

crawler_log = logging.getLogger('Crawler log')
FORMAT = logging.Formatter('%(levelname)s - %(message)s - %(post_url)s')
LOG_FILE_HANDLER = logging.FileHandler('../log/crawler.log', mode = 'w+')
LOG_FILE_HANDLER.setFormatter(FORMAT)
crawler_log.addHandler(LOG_FILE_HANDLER)

def crawl_context(post):

    url = post['post_url']
    response = request(url)

    soup = BeautifulSoup(response, 'html.parser')

    # Parse heading
    try:
        heading = soup.find('h1').text
    except:
        crawler_log.error('No heading', extra=post)
        heading = ''
    # print("Parsed heading")
    # Parse caption
    captions = soup.findAll('figcaption')
    if len(captions) == 0:
        caption = ''
    elif len(captions) == 1:
        caption = captions[0].text
    else:
        # TODO: Choose the correct caption
        crawler_log.warning('Multiple captions', extra=post)
        caption = ''
    # print("Parsed Caption")

    # Parse content
    content = soup.findAll('p')
    context = ''
    for par in content:
        if relevant(par.text, context):
            context += ' ' + par.text

    if not context:
        crawler_log.error('No content', extra=post)    
    # print("Parsed Content")

    return {
        'heading': heading.strip(),
        'caption': caption.strip(),
        'context': context.strip()
    }   

# url = 'https://www.nytimes.com/2019/06/13/us/politics/julian-castro-fox-town-hall.html'
# post = {'post_url':url}
# print(crawl_context(post))