import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(18 , 41)
y = np.zeros(23)
y[7: ] = 1


n = len(x)

w = 0
b = 0
loss = 0
lr = 0.01
dw = 0
db = 0
reg_strength = 1


def sig(z):
    p = 1/(1 + np.exp(-z))
    return p


for epoch in range(10000):
    loss = 0 
    dw = 0
    db = 0
    for xi,yi in zip(x,y):
        z = w*xi + b
        p = sig(z)
        loss += -( ( yi * np.log(p) ) + ( 1 - yi ) * np.log( 1 - p) ) 
        dw += (p - yi)*xi 
        db += (p - yi)
    mean_loss = 1/n * loss + (reg_strength* np.abs(w))
    dw = dw/n +   reg_strength *np.sign(w) 
    db = db/n
    w = w - lr*dw
    b = b - lr*db


print("w : ", w)
print("b : ",b)
print("mean_loss:  ", mean_loss)
print("decision_boundary : " , -b/w)



# with 
# lr = 0.01
# reg_strength = 1
# and
# epochs = 10000


