Feature extraction module
===

# Documentation
`Fourier(BaseEstimator, TransformerMixin)`
 
    A object based on the scikit-learn structure that performs feature extraction in any given signal
    
    ------------------------
    Initialization
    ------------------------
    - fundamental: the fundamental frequency of the signal
    - fs: sampling frequency of the input signal
    - window: range to look for a given harmonic
    - harmonics: tuple containing the multiples of fundamental that ought to be used.

    ------------------------
    Methods
    ------------------------
    
    > transform(df)

    Parameters:
    df: dataframe of the signal that ought to be transformed
    -----
    Returns:
    - dict: a dictonary variable containing the following fields: 
        {'fft': the transformed signal into frequency domain.,
        {'frequency': the values of found frequency according to the given harmonics in Hertz (Hz),
        'features': the feature array,
        'fetures_vector': the feature array of the calculated frequency values
        }
    -----------------


`HOS(BaseEstimator, TransformerMixin)`
 
    A object based on the scikit-learn structure that performs feature extraction in any given signal
    
    ------------------------
    Initialization
    ------------------------
    None

    ------------------------
    Methods
    ------------------------
    
    > transform(df)

    Parameters:
    df: dataframe of the signal that ought to be transformed
    -----
    Returns:
    - dict: a dictonary variable containing the following fields: 
        {'rms': the rms value of the signal,
        {'variance': the variance value of the signal,
        'skewness': the skewness value of the signal,
        'kurtosis': the kurtosis value of the signal,
        'features': the feature array
        }
    -----------------