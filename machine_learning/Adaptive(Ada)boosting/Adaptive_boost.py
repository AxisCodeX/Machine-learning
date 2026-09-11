import numpy as np
import pandas as pd


data = {
    "exam_score": [
        45, 52, 58, 61, 65,
        67, 70, 72, 75, 78,
        80, 82, 85, 87, 90,
        92, 94, 55, 68, 76
    ],

    "study_hours": [
        1, 2, 2, 3, 3,
        4, 4, 5, 5, 6,
        6, 7, 7, 8, 8,
        9, 10, 8, 2, 6
    ],

    "attendance": [
        60, 65, 70, 72, 75,
        78, 80, 82, 85, 86,
        88, 90, 91, 93, 94,
        96, 98, 95, 68, 84
    ],

    "projects": [
        0, 0, 1, 1, 1,
        1, 2, 2, 2, 2,
        3, 3, 3, 4, 4,
        4, 5, 4, 0, 3
    ],

    "admitted": [
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 1,
        1, 1, 1, 1, 1,
        1, 1, 0, 0, 1
    ]
}

df = pd.DataFrame(data)
X = df.drop(columns="admitted")


Y = df["admitted"]


class Stump:
    def __init__(self,feature,alpha ,threshold,left_node,right_node):
        self.feature = feature
        self.threshold = threshold
        self.left_node = left_node
        self.right_node = right_node
        self.alpha = alpha
    
    def make_prediction(self,target):
        def predict(dt,target):
            if target[dt.feature]<= dt.threshold:
                return (1*self.alpha)
            else:
                return (-1*self.alpha)
        prediction = target.apply(lambda row: predict(self,row), axis= 1)
        return prediction.to_numpy() 

class Leaf:
    def __init__(self ,prediction ,is_leaf=True):
        self.prediction = prediction

def create_forest(features , target,n_estimator = 1):
    sample_weights= np.full_like(target,(1/features.shape[0]),dtype=np.float32)
    forest = []
    while len(forest) < n_estimator:
        stump = create_stump(features.to_numpy(),target.to_numpy(),features.columns,sample_weights)
        if stump.alpha <= 0:
            continue
        mask = ((np.array(features[stump.feature]) <= stump.threshold).astype(int) == np.array(target))
        sample_weights[~mask] *= np.exp(stump.alpha)
        sample_weights[mask]*= np.exp(-stump.alpha)
        sample_weights = sample_weights/sample_weights.sum()
        forest.append(stump)
    return forest
    


def find_split(X,Y,sample_weights):
    unique = np.unique(X)
    if np.array_equal(unique , np.array([0,1])):
        thres = np.array([0.5])
    else:
        new_x = np.sort(X)
        thres = (new_x[1:] + new_x[:-1])/2


    prediction = (X <= thres[: , None]).astype(int)
    
    mask = prediction == Y
    errors = np.where(~mask , sample_weights, 0).sum(axis = 0)
    best_split_idx = errors.argmin()
    threshold = thres[best_split_idx]
    total_error = errors[best_split_idx]
    return threshold , total_error
    

def ada_boost(forest,target):
    prediction_accumulator = np.zeros((target.shape[0]))
    for tree in forest:
        prediction = tree.make_prediction(target)
        prediction_accumulator = prediction_accumulator+ prediction
    
    result = np.sign(prediction_accumulator)
    result[result == -1] = 0
    return result
    

def create_stump(X,Y,feature_names,sample_weights):
    df = pd.DataFrame(columns=["threshold","total_error","feature"])
    for idx,col in enumerate(X.T):
        threshold , total_error = find_split(col,Y,sample_weights)
        f = feature_names[idx]
        df.loc[idx] = [threshold,total_error,f]
    best_ft_idx = df["total_error"].argmin()
    total_error = df["total_error"][best_ft_idx]
    best_ft = df["feature"][best_ft_idx]
    threshold = df["threshold"][best_ft_idx]
    alpha = 1/2 * np.log((1 - (total_error + 1e-15))/(total_error + 1e-15))

    return Stump(feature=best_ft,threshold=threshold,left_node=Leaf(prediction=1), right_node=Leaf(prediction=0),alpha=alpha)
    
    


if __name__ == "__main__":
    forest = create_forest(X,Y,3)
    print(forest)
    prediction = ada_boost(forest,X)
    print(prediction)