import tensorflow as tf 
import sys
import numpy as np 
import pandas as pd 
from tqdm import tqdm 
import scrape

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Use case: scrape.py <params file> <search term> <write location>')
        quit()
    
    scrape.generate_dataset(sys.argv[1], sys.argv[2], sys.argv[3])
