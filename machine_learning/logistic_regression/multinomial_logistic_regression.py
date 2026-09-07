import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split




data = pd.read_csv("machine_learning/dataset/wine/wine.data",header=None)

columns = [
    "class",
    "alcohol",
    "malic_acid",
    "ash",
    "alcalinity_of_ash",
    "magnesium",
    "total_phenols",
    "flavanoids",
    "nonflavanoid_phenols",
    "proanthocyanins",
    "color_intensity",
    "hue",
    "od280_od315",
    "proline"
]


data.columns = columns

data[["class_1","class_2","class_3"]] = data.apply(lambda row : [1,0,0] if row["class"] == 1 else [0,1,0] if row["class"] == 2 else [0,0,1], axis = 1,result_type="expand")

X = data.iloc[:, 1:-3 ].to_numpy()
Y = data.iloc[:, -3:].to_numpy()



train_x , test_x , train_y , test_y = train_test_split(X,Y,test_size=0.3 , random_state=42)


n = train_x.shape[0]


W = np.zeros((train_x.shape[1] , train_y.shape[1]))
b = np.zeros(train_y.shape[1])
lr  = 0.00001


def softmax(Z):
    Z = Z - Z.max(axis = 1)[: , None]
    P = np.exp(Z)/ np.exp(Z).sum(axis = 1)[: ,None]
    return P

for epoch in range(50000):
    Z = train_x @ W + b
    P = softmax(Z)
    loss = -1/n *  np.sum( np.log(np.clip(((train_y * P).sum(axis = 1)) , 1e-15,1)))
    dw = 1/n * train_x.T @( P - train_y)
    db = 1/n * (P - train_y).sum(axis = 0)

    W = W - lr* dw
    b = b - lr*db


print("X: ", train_x.shape)
print("W " ,W.shape)
print("train_y : ",train_y.shape)
Z= train_x @ W + b

y = train_y.argmax(axis = 1)
prediction = Z.argmax(axis = 1)
total_prediction = train_y.shape[0]
matched_prediction = prediction == y
accuracy = matched_prediction.sum()/total_prediction
print("training_accuracy : ", accuracy)


y_test = test_y.argmax(axis = 1)
total_prediction_test = y_test.shape[0]
Z_test = test_x @ W + b
predict_test = np.argmax(Z_test, axis = 1)
accuracy_test = (predict_test == y_test).sum() / total_prediction_test
print("test_accuracy : ", accuracy_test)


acutal_0_predicted_0 = ((y_test == 0) & (predict_test == 0)).sum()
acutal_0_predicted_1 = ((y_test == 0) & (predict_test == 1)).sum()
acutal_0_predicted_2 = ((y_test == 0) & (predict_test == 2)).sum()

acutal_1_predicted_0 = ((y_test == 1) & (predict_test == 0)).sum()
acutal_1_predicted_1 = ((y_test == 1) & (predict_test == 1)).sum()
acutal_1_predicted_2 = ((y_test == 1) & (predict_test == 2)).sum()

acutal_2_predicted_0 = ((y_test == 2) & (predict_test == 0)).sum()
acutal_2_predicted_1 = ((y_test == 2) & (predict_test == 1)).sum()
acutal_2_predicted_2 = ((y_test == 2) & (predict_test == 2)).sum()

confusion_matrix = np.array([
    [acutal_0_predicted_0 , acutal_1_predicted_0 , acutal_2_predicted_0],
    [acutal_0_predicted_1 , acutal_1_predicted_1  , acutal_2_predicted_1],
    [acutal_0_predicted_2 , acutal_1_predicted_2 , acutal_2_predicted_2]
])
# cm = np.zeros((3,3))
# np.add.at(cm , (predict_test , y_test) , 1)
print(confusion_matrix)
precision = np.diag(confusion_matrix) / confusion_matrix.sum(axis = 1)
recall = np.diag(confusion_matrix) / confusion_matrix.sum(axis = 0)
f1 = (2 * precision * recall)/(precision + recall)
print("precision : ", precision)
print("recall : ", recall)
print("f1 : ", f1)
print(np.diag(confusion_matrix).sum() / np.sum(confusion_matrix))



#                         class_0       class_1         class_2

# predicted_class 0


# predicted_clas 1


# predicted_class 2
