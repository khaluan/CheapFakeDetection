# # Initialize google api key, sadly no credit card available
# import os
# if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

# print("Config complete")


ANNOTATION_DIR = '/root/thesis/benchmark/cosmos_anns_acm/acm_anns'
IMAGE_DIR = '/root/thesis/benchmark/cosmos_anns_acm/acm_anns/'
CONTEXT_DIR = '../Output/Context'

MAX_POST_PER_SAMPLE = 15