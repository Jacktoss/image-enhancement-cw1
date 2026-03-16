import math
import cmath

import numpy as np

'''
Alpha-Trimmed Mean Filter 
Looking for pixels in the window that are much brighter or darker than the
rest. 
Removing those pixels (in a sorted array the first and last item) of extreme
value.
Static noise on a image can be described as salt and pepper because of black
and white pixels. These skew the mean heavily.

iterating over a padded version of the image, padded with (edge) mode in 
the numpy pad() function which copys the outermost pixel or edge value 
and repeats the values of the pixels on the edge as to not skew the mean
with too much 'new' infromation that might come with padding with a unrelated
value like 0.
'''

def at_mean(x, win):
    if win % 2 == 0 or win < 3 : return -1
    pad_num = win // 2
    x_p = np.pad(x, pad_num, mode='edge')

    xp_h, xp_w = np.shape(x_p)
    i, j = 0, 0
    for r in range(pad_num, xp_h - pad_num):
        for c in range(pad_num, xp_w - pad_num):

            window = x_p[(r-pad_num):(r+pad_num+1), (c-pad_num):(c+pad_num+1)]
            pix_arr = window.flatten()
            pix_arr = np.sort(pix_arr)
            #pix_min = np.min(pix_arr)
            #pix_max = np.max(pix_arr)

            #pix_arr = pix_arr[(pix_arr != pix_min) & (pix_arr != pix_max)]
            
            pix_arr = pix_arr[1:-1] 

            x[i, j] = np.mean(pix_arr)

            j += 1
        i += 1
        j = 0
    return x

































































