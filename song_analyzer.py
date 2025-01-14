#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 8 14:44:33 2024
Based on: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023
Sample input: --filter="ARTIST" --value="Dua Lipa" --order_by="STREAMS" --order="ASC" --limit="6"'
@author: rivera
@author: evanastrasdin
"""

# Import modules
import sys
import argparse as arg
import pandas as pd 
import numpy as np 
from datetime import datetime

    # 1. --data="data.csv" 
    # 2. --filter="ARTIST" 
    # 3. --value="Dua Lipa" 
    # 4. --order_by="STREAMS" 
    # 5. --order="ASC" 
    # 6. --limit="6"

    # Desired output order: released(d, Md, Yr), track_name, artist_name(s), streams
def dateify(data):
    # Reformat date column: Apply applies the lambda function to specd rows of data
    data['released'] = data.apply(lambda x: datetime(x['released_year'], 
    x['released_month'], x['released_day']).strftime('%a, %b %d, %Y'), axis=1)
    return data

def format(data):
    data = dateify(data)
    data = data[[
    'released', 'track_name',
    'artist(s)_name', 'streams']]
    return data

def sort(args, data, order):
    incDec = True if args.order == 'ASC' else False
    if args.limit != None:
        rows = int(args.limit)
        data = data.sort_values(by=order, ascending=incDec).head(rows)
    return data

def handleOrder(args, data):
    if args.order_by == 'STREAMS':
        order = 'streams'
    elif args.order_by == 'NO_SPOTIFY_PLAYLISTS':
        order = 'in_spotify_playlists'
    elif args.order_by == 'NO_APPLE_PLAYLISTS':
        order = 'in_apple_playlists'
    data = sort(args, data, order)
    return data

# Match `column` to column heading, remove irrelevant rows of dataframe
def handleFilter(args, data):
    # Match `column` to relevant column heading
    column = 'released_year' if args.filter == "YEAR" else 'artist(s)_name'
    # Mask data according to whether or not `value` found in `column`
    data = data[data[column].str.contains(args.value)]
    # Return data
    return data

def process(args, data):
    if args.filter != None:
        data = handleFilter(args, data)
    data = handleOrder(args, data)
    data = format(data)
    return data

# Return arguments as parser object 
def getArgs():
    # Create argument parer object
    parser = arg.ArgumentParser(description='Song Analyzer')
    # Add arguments
    parser.add_argument('--data')
    parser.add_argument('--filter')
    parser.add_argument('--value')
    parser.add_argument('--order_by')
    parser.add_argument('--order')
    parser.add_argument('--limit')
    # Return parsed arguments
    return parser.parse_args()

def main():
    # Get input arguments as parser object
    args = getArgs()
    # Retrieve input data as dataframe
    data = pd.read_csv(args.data)
    # Process data according to args
    data = process(args, data)
    # Output data to output.csv
    data.to_csv('output.csv', index=False)

if __name__ == '__main__':
    main()
