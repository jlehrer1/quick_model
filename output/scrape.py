import requests, sys
import json 
import tqdm 
import urllib.request
import os

# To be used in model.py. Generates an image dataset where the directory name is the name of the search term, as specified
# by tf.keras documentation
def generate_dataset(params_file, search_term, write_location):
    path = os.path.join(write_location, search_term) #path to data folder
    other_path = os.path.join(write_location, 'NOT-' + search_term)

    try:
        os.makedirs(path)
    except FileExistsError:
        tqdm.tqdm.write('Directory {} exists, continuing...'.format(path))

    try:
        os.makedirs(other_path)
    except FileExistsError:
        tqdm.tqdm.write('Directory {} exists, continuing...'.format(other_path))

    try:
        params = open(params_file)
    except FileNotFoundError:
        print('Params file not found')
    
    key = params.readline().rstrip()
    cx = params.readline().rstrip()

    tqdm.tqdm.write('Scraping {} images...'.format(search_term))
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
            print('Google CSE API error: {}'.format(response.text))
            quit()
        else:
            for j, responses in tqdm.tqdm(enumerate(response.json()['items'])):
                try:
                    urllib.request.urlretrieve(responses['link'], path + '/{}{}.png'.format(i,j))
                except:
                    continue

    tqdm.tqdm.write('Scraping random images...')
    for i in tqdm.tqdm(range(100)):
        try:
            urllib.request.urlretrieve('https://picsum.photos/256', other_path + '/NOT-{}.png'.format(i))
        except:
            continue