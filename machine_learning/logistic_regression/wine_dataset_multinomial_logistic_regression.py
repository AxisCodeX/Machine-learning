import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_csv("machine_learning/dataset/wine_ordered/WineQT.csv").drop(columns=['Id'])



X = data.iloc[: , :-1].to_numpy()
Y = pd.get_dummies(data['quality']  , dtype=int).to_numpy()

x_train,x_test , y_train , y_test = train_test_split(X , Y , test_size=0.3 , random_state=42)
mean = x_train.mean(axis = 0)
std = x_train.std(axis = 0)
x_train = (x_train - mean) / std

n = x_train.shape[0]
W = np.zeros((Y.shape[1] , X.shape[1]))
b = np.zeros(Y.shape[1])
lr = 0.1

def softmax(Z):
    Z = Z - Z.max(axis = 1)[: , None ]
    P = np.exp(Z) / np.sum(np.exp(Z) , axis = 1)[: , None]
    return P

print("x_train_shape : " , x_train.shape)
print("Weights_shape : ", W.shape)
for epoch in range(20000):
    Z = x_train @ W.T + b
    P = softmax(Z)
    loss = -1/n*  np.sum(np.log((np.clip((P*y_train).sum(axis  = 1), 1e-15 , 1))))
    print("loss : ", loss)
    dw = 1/ n * (P - y_train).T@x_train
    db = 1/n * (P - y_train).sum(axis = 0)
    W -= lr * dw
    b -=  lr*db


print("w : ",W)
print("b : ", b)


Z = x_test @ W.T + b

prediction = np.argmax(Z , axis = 1)
actual_class = np.argmax(y_test , axis = 1)

cm = np.zeros((6,6))
np.add.at(cm , (prediction , actual_class) , 1)

accuracy = np.diag(cm).sum() /cm.sum()
precision = np.diag(cm) / cm.sum(axis = 1)
recall = np.diag(cm ) / cm.sum(axis = 0)
f1 = (2 * precision * recall) / (precision + recall)
mae = np.mean(np.abs(prediction - actual_class))

baseline_prediction = np.full_like(actual_class , 3)
baseline_mae = np.mean(np.abs(baseline_prediction - actual_class))
baseline_accuracy = (baseline_prediction == actual_class).sum() / y_test.shape[0]
print(baseline_prediction)
print(baseline_prediction.shape)
print(actual_class.shape)
print("confusion_matrix \n: ", cm)
print("accuracy : ", accuracy)
print("baseline_accuracy : ", baseline_accuracy)
print("preciison: ", precision)
print("recall: ", recall)
print("f1: ", f1)
print("mae : ", mae)
print("baseline_mae : ", baseline_mae)