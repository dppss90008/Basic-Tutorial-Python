# -*- coding: utf-8 -*-
"""
Author: Xie
Development time: 2020-1-30 
"""

import numpy as np
import matplotlib as mpl

def myfunc(x,y):
    """Introduction of this function"""
    return x+y

if __name__ == '__main__':
    x,y = 3,5
    z = myfunc(x,y)
    print(z)