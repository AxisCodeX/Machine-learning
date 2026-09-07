import numpy as np
import pandas as pd


df = pd.DataFrame({
"exam_score": [
        50, 55, 60, 62, 65,68, 70, 72, 75, 78,80, 83, 85, 88, 90
    ],
"study_hours": [
        2, 4, 1, 6, 3,7, 2, 5, 4, 8,6, 3, 9, 5, 10
    ],
"attendance": [
        0, 1, 0, 1, 0,1, 0, 1, 1, 0, 1, 0, 1, 0, 1
    ],
"admitted": [
        0, 0, 0, 1, 0,1, 0, 1, 1, 0,1, 0, 1, 0, 1
    ]})

X = df.iloc[: ,:3].to_numpy().T
Y = df.iloc[: , -1].to_numpy()


print(X)
thres = (X[: , 1:] + X[: , :-1])/2
print(thres)
mask = X[: , None ,:] < thres[: , : , None]

left_count = np.sum(mask, axis = 1)
right_count = np.sum(~mask , axis = 1)

print(left_count)
print(right_count)
n = len(Y)
left_class_1 = (mask * X[: ,None ,:]).sum(axis = 1)
left_class_0 = left_count- left_class_1


right_class_1 = (~mask * X[: , None , :]).sum(axis = 1)
right_class_0 = right_count - right_class_1


Gini_left = 1 - (np.where(left_count ==0 , np.inf , (left_class_0/left_count)**2 )+ np.where(left_count == 0 , np.inf , (left_class_1/left_count)**2))
Gini_right = 1 - (np.where(right_count==0,np.inf,(right_class_0/right_count))**2) + np.where(right_count==0,np.inf,(right_class_1/right_count)**2)

Gini = 1/n * (np.where(Gini_left == np.inf , np.inf,left_count * Gini_left) + np.where(Gini_right == np.inf , np.inf , right_count * Gini_right))

min_thres_idx = Gini.argmin(axis = 1)
print(min_thres_idx)
