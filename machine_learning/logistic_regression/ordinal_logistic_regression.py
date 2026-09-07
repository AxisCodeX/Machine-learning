import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_csv("machine_learning/dataset/wine_ordered/WineQT.csv")

mapping = {3: 0, 4: 1, 5: 2, 6: 3, 7: 4, 8:5}
data["quality_encoded"] = data["quality"].replace(mapping)
data
print(data)
print("\n\n\n\n\n")
X = data.iloc[ :, : -3].to_numpy()
Y = pd.get_dummies(data["quality_encoded"] , dtype=int).to_numpy()

x_train , x_test , y_train , y_test = train_test_split(X , Y , test_size=0.3 , random_state=42)


n = x_train.shape[0]
mean = x_train.mean(axis = 0)
std = x_train.std(axis = 0)

x_train = (x_train - mean)/std
print("x_train : ", x_train.shape)
print('y_train', y_train.shape)
w = np.zeros(x_train.shape[1])
b = 0
l_r = 0.1
# c-> theresholds
c = np.arange(0,5,dtype=float)


def sigmoid(Z , c ):
    P =  c - np.array(Z)[: , None]
    P = 1/(1 + np.exp(-P))
    return P

def calc_gradient(Q,P,Y):
    def gradient_for_w_and_b(Q,P,Y):
        A =( 1 - Q)
        c1 = A[: , 0]
        c_l = -Q[:,-1]
        A = Q * A
        B = A[: , 1:] - A[: ,:-1]
        B = B / P
        G = np.column_stack((c1,B,c_l))
        return (G * Y).sum(axis = 1)
    def gradient_for_thres(Q,P,Y):
        A = 1 - Q

        B = Q * A
        termA = np.column_stack((-A[:, 0], -B[:, 1:] / P))

        # applies when true class == j+1  (this sample's (j+1)-th class prob uses P_{j+1})
        termB = np.column_stack((B[:, :-1] / P, Q[:, -1]))

        grad = (termA * Y[:, :-1]).sum(axis=0) + (termB * Y[:, 1:]).sum(axis=0)
        return grad
    
    g_w = gradient_for_w_and_b(Q,P, Y)
    g_t = gradient_for_thres(Q,P,Y)
    return g_w , g_t


for epoch in range(10000):
    Z = x_train @ w + b
    q = sigmoid(Z , c)
    probability = q[:, 1:] - q[: , :-1]
    P = np.column_stack((q[:,0] ,probability  , 1 - q[: ,-1 ]))
    loss = -1/n * np.sum(np.log(np.clip((P * y_train).sum(axis = 1),1e-15,1)))
    print("LOSS: ", loss)
    G_w , G_t = calc_gradient(q,probability,y_train)
    dw = 1/n * x_train.T @ G_w
    db = 1/n * G_w.sum()
    dc = 1/n * G_t
    w -= l_r * dw
    b -= l_r*db
    c -= l_r*dc
   


print("W : ", w)
print("b : ", b)
print("C : ", c)


z = x_train@w + b
q = sigmoid(z,c)
P = np.column_stack((q[: ,0] , q[: , 1: ] - q[: , :-1] , 1 - q[: , -1]))

prediction = P.argmax(axis = 1)
actual_class = y_train.argmax(axis = 1)
total_prediction = y_train.shape[0]

accuracy = (prediction == actual_class).sum()/total_prediction
print("train_accuracy : ", accuracy)
print("predicted :  ",  np.bincount(prediction, minlength=6))
print("actual : ",np.bincount(actual_class, minlength=6))


#oridnal error
mae = np.mean(np.abs(prediction - actual_class))
print("mae :", mae)
baseline_prediction = np.full_like(
    actual_class,
    2
)

baseline_mae = np.mean(
    np.abs(baseline_prediction - actual_class)
)

print("naseline : ",baseline_mae)

#on test_set

x_test = (x_test - mean) / std

z_test = x_test@w +b
q = sigmoid(z_test,c)
P_test = np.column_stack((q[: , 0] , q[: ,1:] - q[: , :-1] , 1- q[: , -1]))
prediction_test = P_test.argmax(axis = 1)
actual_test = y_test.argmax(axis = 1)
no_of_prediction_test = y_test.shape[0]
accuracy_test = (prediction_test == actual_test).sum() / no_of_prediction_test
print("predicted_test ", np.bincount(prediction_test , minlength=6))
print("actual_test : ", np.bincount(actual_test , minlength=6))
print("test_accuracy  : ", accuracy_test)

cm = np.zeros((6,6))
np.add.at(cm , (prediction_test , actual_test), 1)
print("confusion_matrix : ", cm)
precision_test = np.diag(cm) / cm.sum(axis = 1)
recall = np.diag(cm) / cm.sum(axis = 0)
f1 = (2*precision_test*recall)/(precision_test + recall)

print("test_precision : ", precision_test)
print("recall : ", recall)
print("f1 : ", f1)


test_mae = np.mean(
    np.abs(prediction_test - actual_test)
)
print("test_mae : ", test_mae)