import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# np.random.seed(1234)


# x = np.random.randint(0,200,500)
# o_std = x.std()
# o_mean = x.mean()
# y = 2*x + np.random.randint(0,50,500)

# w = 2
# b = 1
# l_r = 0.1
# n = len(x)
# x = (x - x.mean())/x.std()
# for epoch in range(500):
#     y_pred = w*x + b
#     error = y_pred - y
#     loss = np.mean(error**2)
#     dw = 2/n * (x * error).sum()
#     db = 2/n * ( error).sum()

#     w = w - l_r * dw
#     b = b- l_r * db
# b = b - (w * o_mean)/o_std
# w = w/o_std

# print("w: ",w)
# print("b:",b)
# print("loss: ",loss)

arr = np.arange(1,13).reshape(4,3)
w = np.arange(1,4)
print(arr.shape)
print(w.shape)

print((arr @ w).shape)