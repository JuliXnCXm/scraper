import pandas as pd
import numpy as np
import os
import argparse


def main(filename):
    df = pd.read_csv(filename)
    df.astype({
        'unitMinPrice': 'float64',
        'valoration': 'float64',
        'delivery_fee': 'float64',
        'delivery_time_min': 'int64',
        'delivery_time_max': 'int64'})

    df['delivery_fee'] = df['delivery_fee'].apply(lambda x: x/100)
    df = df.reindex(columns=['restaurant_name', 'dish_name',
                        'details', 'categories', 'unitMinPrice', 'valoration', 'delivery_fee', 'delivery_time_min', 'delivery_time_max'])
    filename_clean = filename[0:filename.index('_.csv')]
    df.to_csv('{}_clean.csv'.format(filename_clean),sep=',', index=False, encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                    help= 'The path to the dirty data',
                    type= str)

    arg = parser.parse_args()
    df = main(arg.filename)
