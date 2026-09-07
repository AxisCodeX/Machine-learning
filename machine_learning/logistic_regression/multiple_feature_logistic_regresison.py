import pandas as pd
import numpy as np


data = {
    "exam_score": [
        45, 52, 58, 61, 67, 72, 75, 81, 88, 93,
        49, 55, 63, 69, 74, 79, 84, 90, 96, 57,
        43, 60, 65, 71, 77, 83, 87, 92, 51, 68
    ],

    "study_hours": [
        1.2, 1.5, 2.0, 2.2, 2.8, 3.1, 3.5, 4.0, 4.5, 5.0,
        1.0, 1.8, 2.4, 2.7, 3.0, 3.8, 4.2, 4.7, 5.2, 2.1,
        0.8, 2.5, 2.9, 3.3, 3.6, 4.1, 4.4, 4.9, 1.4, 3.0
    ],

    "attendance": [
        62, 68, 70, 73, 76, 80, 82, 85, 91, 94,
        60, 69, 74, 77, 79, 83, 87, 89, 96, 72,
        58, 75, 78, 81, 84, 86, 90, 93, 65, 80
    ],

    "projects": [
        0, 1, 1, 1, 2, 2, 2, 3, 4, 4,
        0, 1, 1, 2, 2, 3, 3, 4, 5, 1,
        0, 1, 2, 2, 3, 3, 4, 4, 1, 2
    ],

    "admitted": [
        0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 1, 1, 1, 1, 1, 1, 0,
        0, 0, 1, 1, 1, 1, 1, 1, 0, 1
    ]
}

df = pd.DataFrame(data)

X = df[["exam_score","study_hours" , "attendance","projects"]].to_numpy()

X_scaled = (X - X.mean(axis = 0))/X.std(axis = 0) 
Y = df["admitted"].to_numpy()
n = X.shape[0]

W = np.zeros(X.shape[1])
b = 0
loss = 0
lr = 0.001

def sig(z):
    p = 1 /(1 + np.exp(-z))
    return p



for epoch in range(1000):
    loss = 0
    z = X_scaled@W + b
    p = sig(z)
    loss += -1/n * ( ( Y @ np.log(p) ) + ( 1 - Y) @ np.log( 1 - p ))
    dw = 1/n * X_scaled.T @ (p - Y) 
    db = 1/n * (p - Y).sum()

    W = W - lr*dw
    b = b - lr * db

print("W : ", W)
print("b :", b)
print("loss : ", loss)
