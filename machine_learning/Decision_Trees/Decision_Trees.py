import numpy as np


X = np.arange(1,7)
Y = np.array([0,0,0,1,1,1])

n = len(Y)
thres = (X[ 1:] + X[:-1])/2

mask = X[None , :] < thres[:,None]
left_mask = np.where(mask ,  1, 0)
right_mask = np.where(~mask , 1, 0)



left_count = left_mask.sum(axis =1 )
right_count = right_mask.sum(axis = 1)

left_class1 =( left_mask * Y).sum(axis = 1)
left_class0 = (left_count) - left_class1

right_class1 = (right_mask * Y).sum(axis = 1)
right_class0 = (right_count - right_class1)

print(left_class0)
print(left_class1)

print(right_class0)
print(right_class1)

left_P1 = left_class1 / left_count
left_P0 = left_class0 / left_count


right_P1 = right_class1 / right_count
right_p0 = right_class0 / right_count

Gini_left = 1 - (left_P1**2 + left_P0**2)
Gini_right = 1 - (right_P1**2 + right_p0**2)

print(Gini_left)
print(Gini_right)

Gini_split = 1/n * (Gini_left * left_count + Gini_right * right_count)
split = Gini_split.argmin()
split_thres = thres[split]
print(split_thres)
