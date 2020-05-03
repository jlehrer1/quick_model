import requests, sys, getopt
import json 
import tqdm 
import urllib.request
import os

def generate_dataset(params_file, search_term, write_location):
    if os.path.isdir(write_location) == False:
        try:
            os.mkdir(write_location)
        except OSError:
            print('Attempt to make data directory failed...')
    try:
        params = open(write_location)
    except FileNotFoundError:
         print('params file not found')
    
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
            print('API error: {}'.format(str(response.status_code)))
            quit()
        else:
            for j, responses in tqdm.tqdm(enumerate(response.json()['items'])):
                try:
                    urllib.request.urlretrieve(responses['link'], write_location + '/{}{}.png'.format(i,j))
                except:
                    continue
    