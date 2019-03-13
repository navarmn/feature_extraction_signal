import numpy as np
from scipy import stats
from sklearn.base import BaseEstimator, TransformerMixin


class Fourier(BaseEstimator, TransformerMixin):
    '''
    Nothing yet.
    -------------------
    Nothing yet.
    '''

    def __init__(self, fundamental, fs=1, window=10, harmonics=(1,10,20,30)):
        self.fs = fs
        self.window = window
        self.harmonics = np.array(harmonics)
        self.fundamental = fundamental    

    def fit(self, X):
        return self

    def transform(self, X):
        # transform data to frequency domain using fft
        # TODO: check if signal is 1-D
        # pre-settings:
        L = X.size
        self.resolution = self.fs/L
        frequency = frequency = self.resolution*(np.linspace(0,L/2, num=L/2))
        # Fourier need to be normalized by signal lenght
        buffer = np.abs(np.fft.fft(X)/L)

        x_fft = 2*buffer[:int(L/2)]

        # desired_frequencies = self.fundamental*self.harmonics
        desired_frequencies = self.harmonics
        features_values = []
        frequency_values = []

        for f in desired_frequencies:
            idx = (frequency <= f + (f*self.window)/100) & ((frequency >= f - (f*self.window/100)))
            features_values.append(np.max(x_fft[idx]))
            frequency_values.append(np.max(frequency[idx]))
            # features_values.append(x_fft[np.argmax(frequency[idx])])


        # Output
        output = {}
        output['fft'] = x_fft
        output['frequency'] = frequency
        output['features'] = features_values
        output['features_vector'] = frequency_values

        return output

class HOS(BaseEstimator, TransformerMixin):
    '''
    Nothing yet.
    -------------------
    Nothing yet.
    '''
    def fit(self, X):
        return self

    def transform(self, X):
        # 
        # TODO: check if signal is 1-D
        # 
        # Output
        output = {}
        output['rms'] = np.sqrt(np.mean(np.square(X)))
        output['variance'] = np.var(X, ddof=1)
        output['skewness'] = stats.skew(X)
        output['kurtosis'] = stats.kurtosis(X)

        output['features'] = [np.sqrt(np.mean(np.square(X))),
                              np.var(X, ddof=1),
                              stats.skew(X), 
                              stats.kurtosis(X)]


        return output
