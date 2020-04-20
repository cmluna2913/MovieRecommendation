# for dataframe building
import pandas as pd
import numpy as np
from surprise import Dataset, Reader

# Importing models that I want to run
from surprise.prediction_algorithms.random_pred import NormalPredictor
from surprise.prediction_algorithms.baseline_only import BaselineOnly

# KNN Based Models
from surprise.prediction_algorithms.knns import KNNBasic, KNNWithMeans, KNNWithZScore, KNNBaseline

# Matrix Factorization Based Models
from surprise.prediction_algorithms.matrix_factorization import SVD, SVDpp, NMF

# Will help measure how our models do
from surprise.model_selection import cross_validate

#visualization
import matplotlib.pyplot as plt
import seaborn as sns

def say_hello(n):
    return('hello'*n)