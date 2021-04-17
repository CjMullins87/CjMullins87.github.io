import numpy as np
import pandas as pd
import string
import random
from scipy.stats import binom

def general_form(array):
    """
    This fxn uses scipy.stats to calculate the probability that an observed
    maximum frequency is random and generates a 'general form' for the string
    if the pattern meets a confidence threshhold.
    """
    #Define binomial params as fxns of array space

    #If string is alphanumeric (mixed numbers and letters) it will have values
    #in the alpha columns [10:36]. Setting threshhold at 2 so that the AI has to
    #make two mistakes in interpretation to trigger this calculation.
    if array[:,10:36].sum() >= 2:
        n = array[0].sum()
        p = 1/36
        k = array.max()
        r = 1-binom.cdf(k, n, p)+binom.pmf(k, n, p)

    #If string is numeric (only numbers) it will only have values in the number
    #columns [0:9], which means the alpha columns should be equal to 0. Setting
    #threshhold at 1 so that the the AI can make 1 mistake.
    else:
        n = array[0].sum()
        p = 1/10
        k = array.max()
        r = 1-binom.cdf(k, n, p)+binom.pmf(k, n, p)

    #Generate stock form for string
    form = 'X '*array.shape[0]
    form = form.split()

    #Special case of high confidence
    if r < 0.001:

        #Retrieve position of k
        rows, columns = np.where(array == k)

        #Translate K
        for index, row in enumerate(rows):
            if columns[index] >= 10:
                form[row] = chr(columns[index]+87)
            else:
                form[row] = str(columns[index])

    return ''.join(form)
