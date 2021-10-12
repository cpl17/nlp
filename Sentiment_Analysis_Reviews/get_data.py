#!usr/bin/python3

import pandas as pd
import os
from zipfile import ZipFile
import shutil

# Note: Must have a kaggle api and store kaggle.json file in ~./kaggle

# Get dataset from kaggle
os.system("kaggle datasets download -d marklvl/sentiment-labelled-sentences-data-set")


# Extract Files 

file_name = "sentiment-labelled-sentences-data-set.zip"

with ZipFile(file_name, 'r') as zip:
    zip.extractall()


# Read and Combine Separate Datasets 

amazon = pd.read_csv("./sentiment labelled sentences/amazon_cells_labelled.txt",header=None,delimiter='\t',names=['reviews','sentiment'])
amazon['site'] = 'amazon'

yelp = pd.read_csv("./sentiment labelled sentences/imdb_labelled.txt",header=None,delimiter='\t',names=['reviews','sentiment'])
yelp['site'] = 'yelp'

imdb = pd.read_csv("./sentiment labelled sentences/yelp_labelled.txt",header=None,delimiter='\t',names=['reviews','sentiment'])
imdb['site'] = 'imdb'

combined = pd.concat([amazon,yelp,imdb])



# Remove Redundant Data Directory
dir_path = "sentiment labelled sentences"

try:
    shutil.rmtree(dir_path)
except OSError as e:
    print("Error: %s : %s" % (dir_path, e.strerror))


# Make Data Directory and Store Data 
os.makedirs("Data")

combined.to_csv("./Data/Reviews_Short_Sentiment.csv")

