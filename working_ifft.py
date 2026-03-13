
import math
import cmath



'''

supposedly its in reverse but also need to pad it  before
'''


def ifft_one_level(x):

    N = len(x)

    if (N == 1): #base case
        return x
    
    x_even = x[0::2]
    x_odd = x[1::2] 

    E = ifft_one_level(x_even)
    O = ifft_one_level(x_odd)
    '''
    for inverse you need sign change on component
    '''


    out_list = [0] * N

    for k in range(int(N/2)): 
        w = cmath.exp(2j * math.pi * k / N)
        out_list[k] = E[k] + w * O[k]
        out_list[k + N//2] = E[k] - w * O[k]
    
    return out_list


def transpose_2d(matrix):
    """
    keeping the same transpose function
    """

    
    return list(map(list, zip(*matrix)))   # map() returns map objects 





def ifft_2d_image(image_matrix, og_height=None, og_width=None):
    
    if og_height is None or og_width is None:
        raise ValueError("IFFT needs original height and width of image to remove padding. Otherwise add 2 parameters of 0 to continue without de-padding")
    



    rows = len(image_matrix)
    cols = len(image_matrix[0])



    for row in range(rows):
        image_matrix[row] = ifft_one_level(image_matrix[row]) 

    
    image_matrix = transpose_2d(image_matrix)

    for col in range(cols):
        image_matrix[col] = ifft_one_level(image_matrix[col])

    image_matrix = transpose_2d(image_matrix)


    for i in range(rows): # now 
        for j in range(cols): # required for ifft becasue of the normalization factor used to reverse scaling
            image_matrix[i][j] = (image_matrix[i][j] / (rows * cols)).real #iamginary value very small here
    #only real

    if og_height == 0 and og_width == 0: #no padding
        return image_matrix
    

    crop_matrix = []

    for i in range(og_height):
        crop_matrix.append(image_matrix[i][0:og_width])

    return crop_matrix  

