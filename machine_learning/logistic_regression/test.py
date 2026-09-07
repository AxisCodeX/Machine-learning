import numpy as np
import pandas as pd


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
X = df[["exam_score","study_hours" , "attendance","projects"]]
Y = df["admitted"]
def sig(z):
    p  = 1/(1 + np.exp(-z))
    return p


def train_model(X,Y , no_of_features ,epochs ,lr=0.001 ):
    X = X.iloc[: , :no_of_features].to_numpy()
    Y = Y.to_numpy()
    n = X.shape[0]
    X_scaled = (X - X.mean(axis = 0)) / X.std(axis = 0)
    loss = 0
    w = np.zeros(no_of_features)
    b = 0

    for epoch in range(epochs):
        z = X_scaled @ w + b
        p = sig(z)
        loss = -1/n * ( Y @ np.log(p) + (1 - Y) @ np.log(1- p))
        dw = 1/n * X_scaled.T @ (p - Y)
        db = 1/n * (p - Y).sum()

        w -= lr*dw
        b -= lr*db

    prediction = sig(X_scaled @ w + b)
    prediction[prediction >= 0.5 ] = 1
    prediction[prediction <0.5 ] = 0
    print(prediction)
    return w,b,loss


w,b,loss = train_model(X , Y ,4 ,120000,0.01)
print("w : ",w)
print("b : ",b)
print("loss : ", loss)

p = sig(X)


# "exam_score","study_hours" , "attendance","projects"

# model 1 -> only exam score
# w :  [13.89589577]
# b :  5.716709407415745
# loss :  0.028206070239402053
# epoch = 200000 and lr = 0.01  


# model 2 -> only exam score and study_hours
# w :  [7.90317034 8.10636746]
# b :  6.028948225039519
# loss :  0.013415366357475098
# epochs = 150000 and lr = 0.01


# model 3 -> exam score ,study_hour and attendance
# w :  [6.15514222 5.47110654 5.1122579 ]
# b :  5.869706293599454
# loss :  0.013463277805813618
# epochs = 120000 lr = 0.01


# model 4 -> all features (exam score , study_hour , attendance , projects)
# w :  [3.50263768 3.13426793 3.20897091 5.62838991]
# b :  5.990323350444742
# loss :  0.005302437029374088
# epoch = 120000 and lr = 0.01