# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tCyy1G0VX8XU7gzObD6oY44JTiqgWwip
"""

#load the data
import pandas as pd
import numpy as np
import sklearn





data = pd.read_csv("/content/drive/MyDrive/Churn_Modelling.csv")

data.head()

#checking for missing values
data.isnull().sum()

#encoding
from sklearn.preprocessing import LabelEncoder

le=LabelEncoder

data.head()

from sklearn.preprocessing import scale

#ANN creation-Tensorflow and keras
import tensorflow

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense