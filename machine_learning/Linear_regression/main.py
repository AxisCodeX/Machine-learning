## LINEAR REGRESSION
# import numpy as np
# import matplotlib.pyplot as plt

# x=np.array([1,2,3,4,5])
# y=np.array([3,5,7,10,11])


# x_mean = x.mean()
# y_mean = y.mean()


# xy_cov = 0
# x_var = 0
# for xi , yi in zip(x,y):
#     xy_cov += (xi - x_mean) * (yi - y_mean)
#     x_var += (xi - x_mean)**2



# w = xy_cov/x_var

# b = y_mean - w*x_mean
# print("w",w)
# print("b",b)

# y_predicted = w*x +b




# for xi,yi,y_p in zip(x,y,y_predicted):
#     plt.plot([xi,xi],[yi,y_p],ls=":", color = "black")

# plt.scatter(x,y,label="data")
# plt.scatter(x, y_predicted ,label="prediction", color="red", s = 80)
# plt.plot(x,y_predicted,label="best fit line")
# plt.title("linear regression")
# plt.legend()
# plt.xlabel("X = Independent Variable")
# plt.ylabel("Y = OUTPUT")
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

np.random.seed(1234)
x = np.random.randint(0,250 , 500)
y = 2*x + np.random.randint(0,50,500)


x_train , x_test ,y_train , y_test = train_test_split(
    x,y,test_size=0.2 , random_state=42
)

# plt.scatter(x_train , y_train , label = "train", alpha=0.4)
# plt.scatter(x_test , y_test , label = "test" , color = "red")
# plt.show()


# l_r = 0.00004
# dw = 0
# db = 0
# Loss = 0
# t_loss = 0
# n = len(x_train)
# w = 0
# b = 0
# for i in range(50000):
#     dw = 0
#     db = 0
#     Loss = 0
#     for xi,yi in zip(x_train , y_train):
#         y_pred = w*xi + b
#         error = y_pred - yi
#         Loss += error**2
#         dw += 2/n * xi * error
#         db += 2/n * error 
    
#     t_loss = 1/n * Loss
#     w  = w - l_r * dw
#     b =  b - l_r * db

# print("w: ",w)
# print("b:",b)
# print("loss: ", t_loss)


# cov_xy = 0
# cov_x = 0
# x_mean = x_train.mean()
# y_mean = y_train.mean()

# for xi , yi in zip(x_train , y_train):
#     cov_xy += (xi - x_mean) * (yi - y_mean)
#     cov_x += (xi - x_mean)**2

# w = cov_xy / cov_x
# b = y_mean - w*x_mean
# print("w:",w)
# print("b:",bool)