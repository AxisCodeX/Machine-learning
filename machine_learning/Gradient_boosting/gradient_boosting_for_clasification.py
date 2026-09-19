import pandas as pd
import numpy as np

data = {
    "hours_studied": [
        1, 2, 2, 3, 3,
        4, 4, 5, 5, 6,
        6, 7, 7, 8, 8,
        9, 9, 10, 10, 11
    ],

    "attendance": [
        50, 55, 60, 52, 65,
        70, 62, 75, 68, 78,
        72, 85, 80, 88, 82,
        92, 86, 95, 90, 98
    ],

    "passed": [
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ]
}

df = pd.DataFrame(data)

X = df.drop(columns="passed").to_numpy()
Y = df["passed"].to_numpy()



class dt_node:
    def __init__(self , threshold = 0 , f_idx = 0 , left_node = None , right_node = None , prediction = None , is_leaf = False):
        self.threshold = threshold
        self.f_idx = f_idx
        self.left_node = left_node
        self.right_node = right_node
        self.prediction = prediction
        self.is_leaf = is_leaf
    

    def make_prediction(self,target):
        if self.is_leaf:
            return np.full(target.shape[0], self.prediction)

        predictions = np.empty(target.shape[0])
        

        left_mask = target[:, self.f_idx] <= self.threshold
        right_mask = ~left_mask 
        

        if np.any(left_mask):
            predictions[left_mask] = self.left_node.make_prediction(target[left_mask])
            
        if np.any(right_mask):
            predictions[right_mask] = self.right_node.make_prediction(target[right_mask])
            
        return predictions




def sigmoid(z):
    P = 1/(1 + np.exp(-z))
    return P


class Gradient_boost:
    def __init__(self):
        self.initial_raw_score = None
        self.forest = None
        self.learning_rate = None
    
    def train(self, X ,Y , n_estimator=1 ,learning_rate=0.1 , max_depth=8 ):
        initial_raw_score,forest = create_forest(X,Y,n_estimator=n_estimator,learning_rate=learning_rate,max_depth=max_depth)
        self.initial_raw_score = initial_raw_score
        self.forest = forest
        self.learning_rate = learning_rate
    
    def predict(self,samples):
        prediction = np.full(samples.shape[0], self.initial_raw_score)
        for tree in self.forest:
            prediction += (self.learning_rate * tree.make_prediction(samples))
        probablity = sigmoid(prediction)
        probablity[probablity >= 0.5] = 1
        probablity[probablity < 0.5] = 0
        return probablity


def create_forest(X,Y,learning_rate=0.1,n_estimator=1,max_depth=8):
    initial_raw_score = np.log((Y==1).sum()/(Y==0).sum())
    current_raw_score = np.full(Y.shape, initial_raw_score)
    P = sigmoid(initial_raw_score)
    residual = (Y - P)
    forest = np.empty((n_estimator,),dtype=object)
    for i in range(n_estimator):
        tree = create_tree(X,residual,max_depth=max_depth)
        current_raw_score = current_raw_score +   learning_rate * tree.make_prediction(X)
        forest[i] = tree
        probablity = sigmoid(current_raw_score)
        residual = (Y - probablity)
    return initial_raw_score,forest



def create_tree(X,r,max_depth):

    if max_depth <= 0:
        return dt_node(prediction= np.mean(r),is_leaf=True)


    df = pd.DataFrame(columns = ['idx','thres','SSE'])
    for idx,feature in enumerate(X.T):
        unique = np.unique(feature)


        if len(unique) <=1:
            return dt_node(prediction= np.mean(r),is_leaf=True)



        thres , min_SSE = split_node(feature,r)
        df.loc[idx] = [idx , thres , min_SSE]
    parent_SSE = np.sum((r - r.mean())**2)
    min_SEE_idx = df["SSE"].argmin()
    thres = df['thres'][min_SEE_idx]
    idx = df['idx'][min_SEE_idx]
    


    if parent_SSE <= df["SSE"][min_SEE_idx]:
        return dt_node(prediction= np.mean(r),is_leaf=True)


    mask = X[: , int(idx)] <= thres
    left_X = X[mask]
    left_r = r[mask]
    right_X = X[~mask]
    right_r = r[~mask]

    return dt_node(
        threshold = thres,
        f_idx = int(idx),
        left_node = create_tree(left_X , left_r , max_depth= (max_depth - 1)),
        right_node = create_tree(right_X , right_r , max_depth= (max_depth - 1))
    )

def split_node(X,r):
    unique = np.unique(X)
    if np.array_equal(unique , np.array([0,1])):
        thres  = np.array([0.5])
    else : 
        new_x = np.sort(X)
        thres = (new_x[1:] + new_x[:-1])/2
    
    mask = X <= thres[:, None]

    left_split = np.where(mask , r , np.nan)
    right_split = np.where(~mask , r , np.nan)

    left_mean = np.nanmean(left_split,axis = 1)
    right_mean = np.nanmean(right_split,axis = 1)

    left_SSE = np.nansum((left_split  - left_mean[: , None])**2 , axis = 1)
    right_SSE = np.nansum((right_split - right_mean[: , None])**2 , axis = 1)

    split_SSE = left_SSE + right_SSE
    thres_idx = np.argmin(split_SSE)
    thres = thres[thres_idx]
    SSE = split_SSE[thres_idx]
    return thres , SSE


if __name__ =="__main__":
    model = Gradient_boost()
    model.train(X,Y,n_estimator=4,learning_rate=0.4 , max_depth=8)
    prediction = model.predict(X)
    print(prediction)
