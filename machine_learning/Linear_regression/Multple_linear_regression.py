import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "area_sqft": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000],
    "bedrooms":  [2,    2,    3,    3,    4,    4,    5,    5,    6,    6],
    "age_years": [15,   10,    8,    12,    5,    7,    4,    6,    3,    2],
    "price_lakh":[45,   55,   68,   78,   95,   105, 120,   135, 150, 165]
})

X = df[["area_sqft","bedrooms","age_years"]].to_numpy()
o_mean = X.mean(axis = 0)
o_std = X.std(axis = 0)
Y = df["price_lakh"].to_numpy()
W = np.zeros(X.shape[1])
b = 0
l_r = 0.1
n = len(df)

X = (X - X.mean(axis = 0))/X.std(axis=0)
for epoch in range(700):
    y_pred = X @ W  + b #(10,) # prediction for every house 
    error = y_pred - Y # error (10 , ) # deviation for every prediction

    loss =  np.mean(error**2)
    dw = 2/n *( X.T @ error)
    db = 2/n * error.sum()
    W = W- (l_r * dw)
    b = b - (l_r * db)

    print("loss : ",loss)

print("w:",W)
print("b:",b)
print("loss: ",loss)

original_w = W/o_std
o_bias = b - (original_w *o_mean).sum()
print("o_w ", original_w)
print("o_b ", o_bias)