#!/usr/bin/env python3

# Example Usage:
# python3 make_collage.py ~/VLC_stuff/frames/color/ labels_color_inceptionresnetv2.csv
# python3 ../make_collage.py ~/VLC_stuff/frames/Whitman_v_Stanford/ labels_50_color_XCEPTION.csv
# python3 ../make_collage.py ~/VLC_stuff/frames/Whitman_v_Stanford/ labels_30_color_XCEPTION.csv

import argparse
import sys
import os
import numpy as np
import pandas as pd
import csv
from collage import Collage
import glob

MAX_COLLAGE_COLUMNS = 10
MAX_COLLAGE_ROWS = 25
DEFAULT_SIZE = 300
DEFAULT_PADDING = 30
DEFAULT_BACKGOUND_COLOR = '#fafafa'

def get_args( arg_values ):
    parser = argparse.ArgumentParser( prog = 'collage' )
    parser.add_argument( 'path', help = 'base path to image files' )
    parser.add_argument( 'input', help = 'input file name (label file)' )
    parser.add_argument( '-o', '--output', help = 'output file name (collage file)' )
    return parser.parse_args( arg_values[ 1: ] ) # Return everything but the program name

def show_args( args ):
    print( args )

def read_data_file( file_name, sep=',', header='infer', index_col=None ):
    try:
        data = pd.read_csv( file_name, sep = sep, header=header, index_col=index_col )
    except EnvironmentError as e:
        sys.stderr.write( 'error: {}\n'.format( e ) )
        return 1
    return data

def get_first_n_images( data, N, path ):
    images_for_collage = []
    for lbl in data['Label'].unique():        
        examples = data.loc[ data[ 'Label' ] == lbl, 'File' ][ :N ]
        for im in examples:
            images_for_collage.append( path + im )
    return images_for_collage

# -----------------------------------------------


# -----------------------------------------------
#   M A I N   P R O G R A M
# -----------------------------------------------

def main( argv ):
    cfg = get_args( argv )
    show_args( cfg )
    data = read_data_file( cfg.input,sep = '\t' )
    collage_cols = min(
        int( data.groupby( 'Label' ).count().min() )
      , MAX_COLLAGE_COLUMNS
    )
    collage_rows = min(
        len( data['Label'].unique())
      , MAX_COLLAGE_ROWS
    )
    first_n_images = get_first_n_images( data, collage_cols, cfg.path )
    params = {
        'path': cfg.path,
        'images': first_n_images,
        'cols': collage_cols,
        'rows': collage_rows,
        'def_size': DEFAULT_SIZE,
        'def_pad': DEFAULT_PADDING,
        'def_bg_color': DEFAULT_BACKGOUND_COLOR
    }
    collage = Collage(params)
    if cfg.output:
        collage.save_to_file(cfg.output)
    else:
        collage.show()

if __name__ == '__main__':
    sys.exit( main( sys.argv ))
