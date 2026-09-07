import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


np.random.seed(42)
n = 100

area = np.random.randint(1000,3000,n)

rooms = area/ 250 + np.random.normal(0,0.4,n)
bedrooms = rooms/ 2+ np.random.normal(0,0.2,n)

price = (
    0.15 * area
    + 8 * rooms
    + 5 * bedrooms
    + np.random.normal(0, 30, n)
)

X = np.column_stack((area , rooms, bedrooms))


x_train , x_test , y_train , y_test = train_test_split(X , price , test_size= 0.2 , random_state=42)


from sklearn.linear_model import LinearRegression

ols = LinearRegression()
ols.fit(x_train , y_train)



from sklearn.linear_model import Ridge
ridge = Ridge(alpha = 10)
ridge.fit(x_train , y_train)


print(ols.coef_)
print(ridge.coef_)

print(ols.score(x_test, y_test))
print(ridge.score(x_test, y_test))