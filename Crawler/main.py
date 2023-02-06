import logging
from unittest import result
from config import *
from util import read_data, request
from tqdm import tqdm
from rev_search import reverse_image_search_try_catch
from preprocess import preprocess_post
import json
from crawler import crawl_context, crawl_context_raw, parse_content, require_Javascript
import time
from os.path import exists, join    

RAW_DIR = r'D:\Context_raw'

main_log = logging.getLogger('Main log')
FORMAT = logging.Formatter('%(levelname)s - %(message)s - Post %(i)s - Context %(j)s - %(post_url)s')
LOG_FILE_HANDLER = logging.FileHandler('../log/main.log', mode = 'a')
LOG_FILE_HANDLER.setFormatter(FORMAT)
main_log.addHandler(LOG_FILE_HANDLER)

parse_log = logging.getLogger('Parse log')
FORMAT = logging.Formatter('%(levelname)s - %(message)s - Post %(i)s - Context %(j)s - %(post_url)s')
LOG_FILE_HANDLER = logging.FileHandler('../log/parse.log', mode = 'w+')
LOG_FILE_HANDLER.setFormatter(FORMAT)
parse_log.addHandler(LOG_FILE_HANDLER)

if __name__ == '__main__':
    data = read_data()
    
    
    # with open('../Output/url_Jan_17(modified_search).txt', 'w+', encoding='utf8') as file:
    #     for datapoint in tqdm(data):
    #         try:
    #             result = reverse_image_search_try_catch(datapoint['img_local_path'])
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

    # for i in tqdm(range(777, len(data))):

    #     row = eval(content[i])
        
    #     for j, post in enumerate(row):
    #         # start_time = time.time()
    #         try:
    #             context_req, context_sel = '', ''
    #             if post['lang'] == 'en':
    #                 context_req, context_sel = crawl_context_raw(post)
    #             with open(f'../Output/Context_raw/{i}_{j}_req.txt', 'w+', encoding='utf8') as output_file:
    #                 output_file.write(post['post_url'] + '\n')
    #                 output_file.write((context_req))
    #             # with open(f'../Output/Context_raw/{i}_{j}_sel.txt', 'w+', encoding='utf8') as output_file:
    #             #     output_file.write((context_sel))

    #         except Exception as e:
    #             main_log.error(f'Error {e}', extra = {**post, **({'i':i, 'j':j})})
    #             main_log.error('Crawl failed', extra = {**post, **({'i':i, 'j':j})})
            # end_time = time.time()
            # print(f'Elapsed time: {end_time - start_time}')
        # break

    # Stage 3
    for i in tqdm(range(len(content))):
        row = eval(content[i])
        
        
        for j, post in enumerate(row):
            # start_time = time.time()
            try:
                if exists(join(RAW_DIR, f'{i}_{j}_req.txt')):
                    with open(join(RAW_DIR, f'{i}_{j}_req.txt'), 'r', encoding='utf8') as file:
                        url = file.readline()
                        response = file.read()
                    context = parse_content(response, post)
                    context['url'] = url
                if require_Javascript(context):
                    continue
                with open(f"../Context_plain/f'{i}_{j}.txt", 'w+', encoding='utf8') as file:
                    json.dump(context, file=file)

            except Exception as e:
                parse_log.error(f'Error {e}', extra = {**post, **({'i':i, 'j':j})})
                parse_log.error('Crawl failed', extra = {**post, **({'i':i, 'j':j})})
            
