from typing import Dict, List
from bs4 import BeautifulSoup
from util import request
import requests
import os
from config import *
import logging

reverse_log = logging.getLogger('Reverse log')
FORMAT = logging.Formatter('%(levelname)s - %(message)s - %(img_path)s')
LOG_FILE_HANDLER = logging.FileHandler('../log/reverse.log', mode = 'w+')
LOG_FILE_HANDLER.setFormatter(FORMAT)
reverse_log.addHandler(LOG_FILE_HANDLER)

# SEARCH_URL = 'https://www.google.com/searchbyimage?hl=en-US&image_url='
SEARCH_BY_IMG_URL = 'http://www.google.hr/searchbyimage/upload'
BASE_URL = 'https://www.google.com'

def search_result_page(response):
    soup = BeautifulSoup(response, 'html.parser')
    CLASS_NAME = 'isv-r PNCib MSM1fd BUooTd'
    elements = soup.find_all('div', CLASS_NAME)
    assert len(elements) > 0

    result = []
    for div in elements:
        element = div.a.next_sibling
        img = div.a.img
        result.append(
            {
                'post_url' : element.get('href'),
                'title'    : element.get('title'),
                'img_url'  : img.get('src')
            }
        )
        # break
    return result

def search_exception(response: str) -> List[Dict]:
    soup = BeautifulSoup(response, 'html.parser')
    header = soup.find('div', 'normal-header')

    CLASS_NAME = 'g Ww4FFb vt6azd tF2Cxc'
    elements = header.find_next_siblings('div', CLASS_NAME)
    result = []
    for div in elements:
        element = div.div.div.div.a
        result.append(
            {
                'post_url' : element.get('href'),
                'title'    : element.h3.text,
                'img_url'  : ''
            }
        )
        # break
    return result


def search_image(search_url: str) -> List[Dict]:
    """
        Returns: a Lisit of relevant posts url and their title
            Each object in the list consists of 2 properties
                post_url: str, url of the post
                title   : str, name of the post title (to identify the language used in the post)
        
        Parameter search_url: The search url retrieved via get_search_url function
    """
    response = request(search_url)

    try:
        return search_result_page(response)
    except:
        return search_exception(response)


def get_search_url(img_path: str) -> str:
    '''
        Returns: similar image search url, used for search function

        Parameter image_url: the url of the image
    '''
    # Copied from https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request
    searchUrl = 'http://www.google.com/searchbyimage/upload'
    multipart = {'encoded_image': (img_path, open(os.path.join(IMAGE_DIR, img_path), 'rb')), 'image_content': ''}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']

    response = request(fetchUrl)
    soup = BeautifulSoup(response, 'html.parser')
    
    CLASS_NAME = 'O1id0e'
    div = soup.find_all('div', CLASS_NAME)
    
    try:
        search_url = BASE_URL + (div[0].a.get('href'))        
        return search_url
    except Exception as e:
        return fetchUrl

def reverse_image_search(img_path):
    try:
        search_url = get_search_url(img_path)    
        return search_image(search_url)
    except Exception as e:
        reverse_log.error('No image found', extra={'img_path': img_path})
        print(e, img_path)

# Example
# img_url = 'https://upload.wikimedia.org/wikipedia/commons/e/e0/180802_%EB%B6%80%EC%82%B0%EB%B0%94%EB%8B%A4%EC%B6%95%EC%A0%9C_%ED%95%98%ED%95%98_1.jpg'
# print(reverse_image_search('0.jpg'))
