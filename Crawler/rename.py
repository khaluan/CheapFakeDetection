import re
from os import listdir, remove
from os.path import isfile, join
import json

DIR = '../Output/Context_Jan_17'
OFFSET = 107

def parse_name(name):
    result = re.search('([0-9]+)_([0-9]+)', name)
    return int(result.group(1)), int(result.group(2))


onlyfiles = [join(DIR, f) for f in listdir(DIR) if isfile(join(DIR, f))]
result = [[] for _ in range(1000)]
for file in onlyfiles:
    u, v = parse_name(file)
    result[u].append(file)

i = 999
while i >= 0:
    if result[i] != []:
        for file in result[i]:
            u, v = parse_name(file)
            with open(file, 'r', encoding='utf8') as ifile:
                content = ifile.read()
            with open(join(DIR, f'{u + OFFSET}_{v}.txt'), 'w+', encoding='utf8') as ofile:
                ofile.write(content)
            remove(file)
        
    i = i - 1