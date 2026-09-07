import numpy as np


arr  = np.arange(0,12).reshape(2,6)
print(arr)

w = arr[: , 1 : ] + arr[: , :-1]
print(w)