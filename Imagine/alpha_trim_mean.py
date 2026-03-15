import math
import cmath

import numpy as np

'''
'''

def at_mean(x, win):
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

































































