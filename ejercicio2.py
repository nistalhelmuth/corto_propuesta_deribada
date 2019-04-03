import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LogisticRegression


def DG(x,y,O,alfa,costod,costo,max_inter=10000):
    
