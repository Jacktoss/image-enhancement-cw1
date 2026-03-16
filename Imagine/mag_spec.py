
import math
import cmath


def mag_spec(x):
    '''
    '''
    rows = len(x)
    cols = len(x[0])

    mag_matrix = [[0.0] * cols for _ in range(rows)] #preseving complex values

    for row in range(rows):
        for col in range(cols):
            magnitude = abs(x[row][col])
            mag_matrix[row][col] = math.log(magnitude + 1) # using a log scale compresses large values and expands small ones
    #overall improving visibility of frequency components. Spectrum easier to interprest
    #+1 to prevent math.log(0)
    return mag_matrix































































