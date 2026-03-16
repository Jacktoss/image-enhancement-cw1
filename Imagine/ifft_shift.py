import cmath
import math
import numpy as np


def ifft_shift(x):

    np_x = np.array(x)

    x_rows, x_cols = np_x.shape

    '''
    Similar again but refering to same directional space
    but inside each block are differnt values

    '''
 
    tl = np_x[0:x_rows//2, 0:x_cols//2] 
    tr = np_x[0:x_rows//2, x_cols//2:x_cols]
    br = np_x[x_rows//2:x_rows, x_cols//2:x_cols]
    bl = np_x[x_rows//2:x_rows, 0:x_cols//2]

    return np.block([[br, bl], [tr, tl]]).tolist()  # handy .block concatenates 


































































