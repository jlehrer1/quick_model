import requests, sys
import json 
import tqdm 
import urllib.request
import os

# To be used in model.py. Generates an image dataset where the directory name is the name of the search term, as specified
# by tf.keras documentation
def generate_dataset(params_file, search_term, write_location):
    path = write_location + '/{}/'.format(search_term) #path to data folder
    if os.path.isdir(path) == False:
        try:
            print(path)
            os.makedirs(path)
        except OSError:
            print('Attempt to make data directory failed...')

    try:
        params = open(params_file)
    except FileNotFoundError:
         print('Params file not found')
    
    key = params.readline().rstrip()
    cx = params.readline().rstrip()

    for i in tqdm.tqdm(range(1,11)):
        params = {
            ('key', key),
            ('cx', cx),
            ('q', search_term),
            ('searchType', 'image'),
            ('num', 10), #max
            ('safe', 'off'),
            ('start', i),
        }
        response = requests.get('https://www.googleapis.com/customsearch/v1?', params=params)
        if response.status_code >= 400:
            print('Google CSE API error: {}'.format(str(response.status_code)))
            quit()
        else:
            for j, responses in tqdm.tqdm(enumerate(response.json()['items'])):
                try:
                    urllib.request.urlretrieve(responses['link'], path + '/{}{}.png'.format(i,j))
                except:
                    continue
    