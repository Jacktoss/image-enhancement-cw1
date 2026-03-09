import cmath
import math



def dft(x):

    # x list of num
    # "N" = len.x

    X = []
    N = len(x)
    for k in range(len(x)):
        sum_ = 0
        
        for n in range(int(N)):
            sum_ += x[n] * cmath.exp(-2j * math.pi * k * n / N)
         
        X.append(sum_)
    
    return X

y = [1.0, 2.0, 3.0, 4.0]



#print(dft(y))
        



































































