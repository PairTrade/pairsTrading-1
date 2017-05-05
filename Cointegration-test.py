# -*- coding: utf-8 -*-
"""
Created on Fri May 05 11:20:26 2017

How To Use:
    Download data from Yahoo Finance for two stocks. Make sure to have the same
    dates for both stocks and DO NOT alter the format. Make sure to save it as
    a .csv file. At the top of this file put the path to the stock data (fileOne
    and fileTwo variables). Then run the script and the p-value is printed at 
    the bottom.

@author: Max
"""

import csv
import numpy as np
import pandas as pd

import statsmodels
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint

fileOne = "" #<path-to-csv>
fileTwo = "" #<path-to-csv>

def importStockPrices(fileName):
    with open(fileName,'rb') as csvfile:    
        reader=csv.reader(csvfile)
        data=[]
        for row in reader:
            data.append([row])
    
    stacked = np.vstack(data[1:])
    close = stacked[:,5] # using default from yahoo finance download.
    close = np.array(close).astype(np.float) # change from strings to floats.
    return close

def cointegrationTest(stockPricesOne, stockPricesTwo):
    coint_t, pvalue, crit_value = coint(stockPricesOne, stockPricesTwo)
    return pvalue

pricesOne = importStockPrices(fileOne)
pricesTwo = importStockPrices(fileTwo)

pValue = cointegrationTest(pricesOne, pricesTwo)
print "P-value for cointegration test for provided two stocks is: ", pValue