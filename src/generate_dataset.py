from feature_extraction import Fourier
from feature_extraction import HOS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import re
import argparse


def set_label(filename):

    reg_exp = re.compile('\d+')
    number_of_file = int(reg_exp.findall(filename)[0])

    if number_of_file >=0 and number_of_file <=100:
        return 0
    elif number_of_file >=101 and number_of_file <=200:
        return 1
    elif number_of_file >=201 and number_of_file <=300:
        return 2
    elif number_of_file >=301 and number_of_file <=400:
        return 3
    elif number_of_file >=401 and number_of_file <=500:
        return 4
    elif number_of_file >=501 and number_of_file <=600:
        return 5
    elif number_of_file >=601 and number_of_file <=700:
        return 6
    elif number_of_file >=701 and number_of_file <=800:
        return 7
    elif number_of_file >=801 and number_of_file <=900:
        return 8
    elif number_of_file >=901 and number_of_file <=1000:
        return 9
    elif number_of_file >=1001 and number_of_file <=1100:
        return 10
    elif number_of_file >=1101 and number_of_file <=1200:
        return 11
    elif number_of_file >=1201 and number_of_file <=1300:
        return 12
    elif number_of_file >=1301 and number_of_file <=1400:
        return 13
    elif number_of_file >=1401 and number_of_file <=1500:
        return 14
    elif number_of_file >=1501 and number_of_file <=1600:
        return 15


def main(args):

    os.chdir('../data/interim')
    print(os.getcwd())

    # for root, dirs, files in os.walk("data/interim"):  
    label = []

    feat_Fourier = []
    feat_HOS = []

    for filename in os.listdir():
        print('Filename: {}'.format(filename))
        # with open(filename, 'w') as csvfile:

        data_signal =  pd.read_csv(filename, sep="\s+|\s\s", 
                                    header=None, error_bad_lines=False, verbose=False, lineterminator='\n')
            
        ######################################################################## 
        # Feature extracion of Fourier:
        ################################################ ########################

        fund = 1e7
        fs = 50000000.0
        window = 10
        # harmonics = list(np.linspace(1e-20, 1, num=20))
        harmonics = (1e7, 1.5e7, 0.5e7, 0.7e7, 1.25e7, 0.7e7, 0.25e7)
        tf_Fourier = Fourier(fundamental=fund, fs=fs, window=window, harmonics=harmonics)
        buffer_fourier = tf_Fourier.fit_transform(data_signal[1])

        # insert label:
        buffer_fourier['features'].insert(len(buffer_fourier['features']), set_label(filename))
        
        feat_Fourier.append(buffer_fourier['features'])
        
        ######################################################################## 
        # HOS Fourier:
        ######################################################################## 

        tf_HOS = HOS()
        buffer_hos = tf_HOS.fit_transform(data_signal[1])

        # insert label:
        buffer_hos['features'].insert(len(buffer_hos['features']), set_label(filename))
        
        feat_HOS.append(buffer_hos['features'])


        # Feature extracion of Goertzel:


        # Feature extracion of SCM:


    # Save files into a .csv file

    fourier_df = pd.DataFrame(data=feat_Fourier, columns=None)
    hos_df = pd.DataFrame(data=feat_HOS, columns=None)

    output_name = args['name_dataset']

    fourier_df.to_csv('../processed/' + output_name + '_fourier.csv')
    hos_df.to_csv('../processed/' + output_name + '_hos.csv')

if __name__ == '__main__':
    # Asterisk arguments
    parser = argparse.ArgumentParser(description='Features generations to Ultrasson - Prof. Elineudo UFC')
    parser.add_argument('--name-dataset', type=str)
    args = vars(parser.parse_args()) 
    main(args)

print('Done!')

