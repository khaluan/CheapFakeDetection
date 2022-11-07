import logging
from unittest import result
from config import *
from util import read_data, request
from tqdm import tqdm
from rev_search import reverse_image_search
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
    
    # with open('../Output/url.txt', 'w+', encoding='utf8') as file:
    #     for datapoint in tqdm(data):
    #         try:
    #             result = reverse_image_search(datapoint['img_local_path'])
    #             # result = reverse_image_search(datapoint) # Replace the above line with this line in case recover from error
    #             result = preprocess_post(result, remove_irrelevant=False)
    #         except:
    #             pass
    #         file.write(json.dumps(result, ensure_ascii=False))
    #         file.write('\n')

    
    with open('../Output/url_merged.txt', 'r', encoding='utf8') as input_file:
        content = input_file.readlines()
    
    with open('../log/reverse_final.log', 'r', encoding='utf8') as log_file:
        log = log_file.readlines()
    log = list(map(lambda x: x.split(' - ')[-1], log))

    for i in tqdm(range(len(data))):
        if f'public_test_mmsys/{i}.png' in log:
            continue

        row = eval(content[i])
        
        for j, post in enumerate(row):
            try:
                if post['lang'] == 'en':
                    with open(f'../Output/Context_raw/{i}_{j}.html', 'w+', encoding='utf8') as output_file:
                        context = crawl_context_raw(post)
                        output_file.write(json.dumps(context, ensure_ascii=False))
            except:
                main_log.error('Crawl failed', extra={**post, **({'i':i, 'j':j})})
