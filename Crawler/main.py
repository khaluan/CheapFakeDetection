import logging
from config import *
from util import read_data, request
from tqdm import tqdm
from rev_search import reverse_image_search
from preprocess import preprocess_post

from crawler import crawl_context

main_log = logging.getLogger('Main log')
FORMAT = logging.Formatter('%(levelname)s - %(message)s - Post %(i)s - Context %(j)s - %(post_url)s')
LOG_FILE_HANDLER = logging.FileHandler('../log/main.log', mode = 'w+')
LOG_FILE_HANDLER.setFormatter(FORMAT)
main_log.addHandler(LOG_FILE_HANDLER)

if __name__ == '__main__':
    data = read_data()
    
    # with open('../Output/url.txt', 'w+', encoding='utf8') as file:
    #     for datapoint in tqdm(data):
    #         try:
    #             result = reverse_image_search(datapoint['img_local_path'])
    #             result = preprocess_post(result, remove_irrelevant=False)
    #         except:
    #             pass
    #         file.write(str(result))
    #         file.write('\n')
            
    with open('../Output/url_full.txt', 'r', encoding='utf8') as input_file:
        content = input_file.readlines()
    
    with open('../log/reverse_full.log', 'r', encoding='utf8') as log_file:
        log = log_file.readlines()
    log = list(map(lambda x: x.split(' - ')[-1], log))

    for i in tqdm(range(len(data))):
        if f'public_test_mmsys/{i}.png' in log:
            continue

        row = eval(content[i])
        
        for j, post in enumerate(row):
            try:
                if post['lang'] == 'en':
                    with open(f'../Output/Context/{i}_{j}.txt', 'w+', encoding='utf8') as output_file:
                        context = crawl_context(post)
                        output_file.write(str(context))
            except:
                main_log.error('Crawl failed', extra={**post, **({'i':i, 'j':j})})
