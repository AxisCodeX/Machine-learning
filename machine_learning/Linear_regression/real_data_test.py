import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
diabetes = load_diabetes(as_frame=True)

data = diabetes.data
target = diabetes.target


df = data.copy()
df["target"] = target

# print(df.corr()["target"])
# print(df.columns.to_numpy())

# plt.title("correlation graph")
# plt.bar(df.columns.to_numpy(),df.corr()["target"].to_numpy(), 0.8)
# plt.show()


from sklearn.model_selection import train_test_split

X , X_test , Y_train , Y_test = train_test_split(
    data,target, test_size=0.2 , random_state=42
)

X_train = np.column_stack((np.ones(X.shape[0]),X))

theta = np.linalg.solve(X_train.T @ X_train , X_train.T @ Y_train)
print(theta)


from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X,Y_train)
coeff = model.coef_
intercept = model.intercept_
print("coeff" , coeff)
print("intercept :",intercept)

####testing part 