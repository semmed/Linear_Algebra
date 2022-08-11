import numpy as np

def set_limit(x, k=1.1):
    r = np.ptp(x,axis=1).reshape(2,1)/10
    low = np.min(x,axis = 1).reshape(2,1)-r
    high = np.max(x,axis = 1).reshape(2,1)+r
    return np.column_stack((low,high))