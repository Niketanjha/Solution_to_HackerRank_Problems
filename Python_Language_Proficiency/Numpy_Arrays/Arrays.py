#reverse of a string 

import numpy
def arrays(arr):

    return numpy.array(arr,float)[::-1]
    # complete this function
    # use numpy.array

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)
