#!/usr/bin/env python3

import argparse
import sys
import os
import numpy as np
import pandas as pd
import csv
from sklearn.cluster import KMeans

# Example Usage:
# python3 cluster.py features_color_vgg16.csv -k 2 -o labels_color_vgg16.csv

# python3 cluster.py features_color_inceptionresnetv2.csv -k 20 -o labels_color_inceptionresnetv2.csv


# -----------------------------------------------

def get_args( arg_values ):
    parser = argparse.ArgumentParser( prog = 'cluster' )
    parser.add_argument( 'input', help = 'input file name (feature file)' )
    parser.add_argument( '-k', '--clusters', type = int, default = 2, help = 'number of clusters' )
    parser.add_argument( '-o', '--output', help = 'output file name (label file)' )
    return parser.parse_args( arg_values[ 1: ] ) # Return everything but the program name

def show_args( args ):
    print( args )

def get_features( file_name ):
    try:
        data = pd.read_csv( file_name, sep = ',' )
    except EnvironmentError as e:
        sys.stderr.write( 'error: {}\n'.format( e ) )
        return 1
    return data

def cluster( N, features ):
    data = np.array( features.iloc[ :,1: ] )
    data = data.astype( np.float )
    kmeans = KMeans( n_clusters = N ).fit( data )
    df = pd.DataFrame( [ kmeans.labels_.T, features.iloc[:,0]] ).T
    df.columns =  ('Label', 'File')
    return df


def save_labels( data, file_name ):
    try:
            data.to_csv( file_name, sep="\t", index=False )
    except EnvironmentError as e:
        sys.stderr.write( 'error: {}\n'.format( e ) )
        return 1

# -----------------------------------------------
#   M A I N   P R O G R A M
# -----------------------------------------------

def main(argv):
    cfg = get_args( argv )              # Get command-line arguments
    show_args( cfg )                    # Show the arguments
    data = get_features( cfg.input )
    results = cluster( cfg.clusters, data )
    results = results.sort_values( by=['Label', 'File'])
    print( results )
    if cfg.output:
        save_labels( results, cfg.output )

if __name__ == '__main__':
    sys.exit( main( sys.argv ))
