import pandas as pd
import numpy as np
from scipy.stats import mode
from sklearn.model_selection import train_test_split

data = pd.read_csv("machine_learning/dataset/wine_ordered/WineQT.csv").drop(columns=["Id"])



X = data.iloc[: , 0 :11].to_numpy()
Y = pd.get_dummies(data["quality"] , dtype=int).to_numpy()


x_train, x_test , y_train , y_test =  train_test_split(X,Y,test_size=0.3,random_state=42)
mean = x_train.mean(axis = 0)
std = x_train.std(axis = 0 )

x_train = (x_train - mean)/std
x_test = (x_test - mean) /std

K = 29

print("x_train :",x_train.shape)
print("x_test : ", x_test.shape)

distance = x_test[: , None ,: ] - x_train[None, : , :]
closest = np.sqrt((distance ** 2).sum(axis = 2)).argsort(axis = 1)
nearest_k = closest[: , :K]
z = y_train[nearest_k]
classes = z.argmax(axis = 2)
prediction = np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis=1, arr=classes)
print(prediction)

actual_classes = y_test.argmax(axis = 1)

confusion_matrix = np.zeros((6,6))
np.add.at(confusion_matrix, (prediction,actual_classes),1)

accuracy = np.diag(confusion_matrix).sum() /np.sum(confusion_matrix)
precision = np.diag(confusion_matrix) / np.sum(confusion_matrix , axis = 1)
recall = np.diag(confusion_matrix) / np.sum(confusion_matrix , axis = 0)
f1 = (2 * precision *recall )/(precision + recall)
mae = np.mean(np.abs(prediction - actual_classes))

base_line_prediction = np.full_like(prediction , 3 )
base_line_mae = np.mean(np.abs(base_line_prediction - actual_classes))


print("K : ", K)
print(confusion_matrix)
print("accuracy : ", accuracy)
print("precision : ", precision)
print("recall : ", recall)
print("f1 : ", f1)
print("mae : ", mae)
print("baseline mae from predicting only class 3 : ", base_line_mae) # from predicting only class 3

