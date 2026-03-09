
import math
import cmath






'''
Find magnitude and phase

what is magnitude spectrum
shows amplitude of each frequnecy component in an image when FFT'd.
It is the absolute value of each complex output.
for normal number x magnitued = |x| 

for any complex number a+bj  ->  sqrt(real^2 + imaginary^2) is magnitude
given imaginary = sqrt(-1), sqrt(-1)^2 is squared and so posotive, the square
roots of any positive number are real positive values.


python has abs() function working for complex numbers

magnitude spectrum is a 2d array where each element is the magnitude of
a corresponding complex number
'''

def mag_spec(x):

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































































