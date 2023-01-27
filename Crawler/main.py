import logging
from unittest import result
from config import *
from util import read_data, request
from tqdm import tqdm
from rev_search import reverse_image_search_try_catch
from preprocess import preprocess_post
import json
from crawler import crawl_context_raw

main_log = logging.getLogger('Main log')
FORMAT = logging.Formatter('%(levelname)s - %(message)s - Post %(i)s - Context %(j)s - %(post_url)s')
LOG_FILE_HANDLER = logging.FileHandler('../log/main.log', mode = 'w+')
LOG_FILE_HANDLER.setFormatter(FORMAT)
main_log.addHandler(LOG_FILE_HANDLER)

if __name__ == '__main__':
    data = read_data()
    
    ################# FOR ERRORS #################################
    # with open('../log/reverse_full.log', 'r') as file:
    #     data = file.readlines()
    # data = list(map(lambda x: x.split('-')[-1].strip(), data))
    ##################################################################
    
    # with open('../Output/url_Jan_17(modified_search).txt', 'w+', encoding='utf8') as file:
    #     for datapoint in tqdm(data):
    #         try:
    #             result = reverse_image_search(datapoint['img_local_path'])
    #             result = preprocess_post(result, remove_irrelevant=False)
    #         except:
    #             pass
    #         file.write(str(result))
    #         file.write('\n')
        


    # Stage 2:         
    with open('../Output/url_Jan_17(modified_search).txt', 'r', encoding='utf8') as input_file:
        content = input_file.readlines()
    print(len(content))

    # with open('../log/reverse_full.log', 'r', encoding='utf8') as log_file:
    #     log = log_file.readlines()
    # log = list(map(lambda x: x.split(' - ')[-1], log))

    # for i in tqdm(range(812, len(data))):

    #     row = eval(content[i])
        
    #     for j, post in enumerate(row):
    #         try:
    #             if post['lang'] == 'en':
    #                 with open(f'../Output/Context_Jan_17/{i}_{j}.txt', 'w+', encoding='utf8') as output_file:
    #                     context = crawl_context(post)
    #                     output_file.write(json.dumps(context))
    #         except:
    #             main_log.error('Crawl failed', extra={**post, **({'i':i, 'j':j})})
