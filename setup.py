#Set up environment Import neccessary packages.
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from scipy.stats import gaussian_kde
import os
import numpy as np
import tensorflow as tf # This code has been tested with TensorFlow 1.6
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from sklearn.preprocessing import MinMaxScaler

from sklearn.metrics import mean_squared_error
%matplotlib inline
