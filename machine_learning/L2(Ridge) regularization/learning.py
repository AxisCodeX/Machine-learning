import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


x = np.arange(1,10)
y = 2*x + np.random.randint(0,10,9)
n = len(x)
w = 0
b = 0
dw = 0
db = 0
lr = 0.01
rs = 1 # ridig strength 
loss = 0
for epoch in range(100):
    loss = 0
    dw = 0
    db = 0
    for xi,yi in zip(x,y):
        y_pred = w* xi + b
        error = ( y_pred - yi )
        loss += error 
        dw += 2/n * ( xi * error)
        db += 2/n * error

    mse = 1/n * loss
    w -= lr * dw
    b -= lr * db


print("mse :",mse )
print("w: ",w)
print("b:",b)


# y_pred = w * x + b
# fig,ax = plt.subplots(1,2)

# ax[0].set_title("Ordinary lest square")
# ax[0].set_xlabel("X= Independent Variable")
# ax[0].set_ylabel("Y = Trarget")
# ax[0].scatter(x,y) #training data
# ax[0].plot(x,y_pred ,color="red")#best fit line 
# plt.show()
