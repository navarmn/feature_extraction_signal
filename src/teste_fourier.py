from feature_extraction import Fourier

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_2 = pd.read_csv('./data/interim/ascan1600.dat', sep="\s+|\s\s", 
            header=None, error_bad_lines=False, verbose=False, lineterminator='\n')

# data_2 = pd.read_csv('../data/interim/ascan0001.dat', sep="\s+|\s\s", 
            # header=None, error_bad_lines=False, verbose=False, lineterminator='\n')

fe_fourier = Fourier(fs=50000000.0, harmonics=(409,20,50), fundamental=24414.0625, window=10)

data_fft = fe_fourier.fit_transform(data_2[1])
print(data_fft['features'])

plt.plot(data_fft['frequency'], data_fft['fft'])
plt.show()