import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error



np.random.seed(42)
n = 10000
df = pd.DataFrame({
    "area_sqft": np.random.randint(500, 4000, n),
    "bedrooms": np.random.randint(1, 7, n),
    "age_years": np.random.randint(0, 40, n),
    "distance_km": np.random.uniform(1, 30, n),
    "floor": np.random.randint(1, 21, n)
})

df["price"] = (
    0.05 * df["area_sqft"]
    + 4.0 * df["bedrooms"]
    - 0.15 * df["age_years"]
    - 0.8 * df["distance_km"]
    + 1.5 * df["floor"]
    + np.random.normal(0, 5, n)
)



X = df[["area_sqft","bedrooms","age_years","distance_km","floor"]].to_numpy()
Y = df["price"].to_numpy()

x_train , x_test , y_train , y_test = train_test_split(X,Y,test_size=0.2 , random_state=42)

x_train_mean = x_train.mean(axis = 0)
x_train_std  = x_train.std(axis = 0)
n = len(x_train)
x_train = (x_train - x_train_mean) / x_train_std

W_scaled = np.zeros(x_train.shape[1])
b_scaled = 0
l_r = 0.01

for epoch in range(4350):
    y_p =  x_train @ W_scaled + b_scaled 
    error = y_p - y_train
    loss = np.mean(error**2)
    dw = 2/n * (x_train.T @ error) 
    db = 2/n * (error).sum()

    W_scaled = W_scaled - (l_r * dw)
    b_scaled = b_scaled - (l_r * db)
    print("loss : ",loss)

print("W_scaled : ",W_scaled)
print("b_scaled : ", b_scaled)
print("loss : ", loss)

W_original = W_scaled / x_train_std
b_original = b_scaled - (W_original * x_train_mean).sum()

print("W_original : ", W_original)
print("b_original : ",b_original)



# my model with l_r = 0.01
# W_scaled :  [50.60804142  6.94024326 -1.73576691 -6.66894329  8.55450618]
# b_scaled :  126.89513562751512
# loss :  25.26976424639894
# W_original :  [ 0.05001145  4.05555695 -0.15073085 -0.79484443  1.4907226 ]
# b_original :  -0.20457042043011597

model = LinearRegression()
model.fit(x_train , y_train)
W_model = model.coef_
b_model = model.intercept_



print("W_model : ", W_model)
print("b_model : ",b_model)




####testing
print("testing")
print("testing")
print("testing")
print("testing")
x_test = (x_test - x_train_mean) / x_train_std

## my model 
y_predict = x_test @ W_scaled + b_scaled
error = y_predict - y_test
loss_test = np.mean(error**2)

print("test_loss : ", loss_test)

##sklearn 
y_predict_model = model.predict(x_test)
loss_test_model = mean_squared_error(y_test , y_predict_model)
print("test_loss_model : ", loss_test_model)


# #my model
# W_scaled :  [50.60804142  6.94024326 -1.73576691 -6.66894329  8.55450618]
# b_scaled :  126.8951356275152
# loss :  25.26976424639894
# W_original :  [ 0.05001145  4.05555695 -0.15073085 -0.79484443  1.4907226 ]
# b_original :  -0.2045704204301586
# #sklearn
# W_model :  [50.60804142  6.94024326 -1.73576691 -6.66894329  8.55450618]
# b_model :  126.89513562751556
# testing
# testing
# testing
# testing
# #my model 
# test_loss :  25.07602404823222
# # sklearn
# test_loss_model :  25.076024048232217