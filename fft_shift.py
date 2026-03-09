
import cmath
import math
import numpy as np




'''
i think i want to transpose the complex matrix  but in a way
where the transposed grid is a quadrant of the original matrix


how to get quarant of a matrix? 

using a numpy array put have totatl rows and cols
'''

def fft_shift(x):

    np_x = np.array(x)

    x_rows, x_cols = np_x.shape

    '''
    *clockwise starting top right"

    [0:N//2, 0:N//2] (top-left)
    [0:N//2, N//2:N] (top-right)
    [N//2:N, N//2:N] (bottom-right)
    [N//2:N, 0:N//2] (bottom-left)
    '''
 
    tl = np_x[0:x_rows//2, 0:x_cols//2] 
    tr = np_x[0:x_rows//2, x_cols//2:x_cols]
    br = np_x[x_rows//2:x_rows, x_cols//2:x_cols]
    bl = np_x[x_rows//2:x_rows, 0:x_cols//2]
    """
    tl = np.transpose(tl) # along y=x
    tr = np.rot90(np.transpose(tr), 2) # along y=-x
    br = np.transpose(br)
    bl = np.rot90(np.transpose(bl), 2)
    """


    return np.block([[br, bl], [tr, tl]]).tolist()  # handy .block concatenates 


































































