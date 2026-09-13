import numpy as np
import pandas as pd

data = {
    "area": [
        50, 60, 70, 80, 90,
        100, 110, 120, 130, 140,
        150, 160, 170, 180, 190,
        200, 210, 220, 230, 240
    ],

    "age": [
        20, 18, 22, 15, 17,
        12, 14, 10, 13, 8,
        11, 7, 9, 6, 5,
        4, 6, 3, 5, 2
    ],

    "distance": [
        15, 14, 13, 12, 11,
        10, 9, 8, 9, 7,
        6, 7, 5, 6, 4,
        5, 3, 4, 2, 1
    ],

    "price": [
        42, 47, 49, 56, 58,
        65, 67, 73, 74, 81,
        85, 91, 94, 101, 105,
        112, 116, 123, 128, 135
    ]
}

df = pd.DataFrame(data)

X = df.drop(columns="price").to_numpy()
Y = df["price"].to_numpy()

class dt_node:
    def __init__(self,threshold=0,f_idx=0,feature=None,left_node = None , right_node = None , is_leaf = False , prediction=None):
        self.threshold = threshold
        self.f_idx = f_idx
        self.feature = feature
        self.left_node = left_node
        self.right_node = right_node
        self.is_leaf = is_leaf
        self.prediction = prediction

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
            




def find_split(feature,residuals):
    unique = np.unique(feature)
    if len(unique) <=1:
        return 0,np.inf
    if np.array_equal(unique,np.array([0,1])):
        thres = np.array([0.5])
    else:
        new_x = np.sort(feature)
        thres = (new_x[1:]+new_x[:-1])/2
    
    mask = feature <= thres[:,None]

    left_split = np.where(mask , residuals ,np.nan)
    right_split = np.where((~mask) , residuals , np.nan)

    left_mean = np.nanmean(left_split,axis=1)
    right_mean = np.nanmean(right_split , axis = 1)

    left_SSE = np.nansum((left_split - left_mean[:, None])**2, axis=1)
    right_SSE = np.nansum((right_split - right_mean[:, None])**2, axis=1)
    split_SSE = left_SSE + right_SSE
    thres_idx = split_SSE.argmin()
    thres = thres[thres_idx]
    return thres,split_SSE[thres_idx]




def create_tree(X,r,max_depth):
    if max_depth <=0:
        return dt_node(
                    threshold=0,
                    feature=None,
                    is_leaf=True,
                    prediction=np.mean(r)
                )
    df = pd.DataFrame(columns=["idx","thres","SSE"])
    for idx,features in enumerate(X.T):
        if(len(features) <= 1):
            return dt_node(
                    threshold=0,
                    feature=None,
                    is_leaf=True,
                    prediction=np.mean(r)
                )
        thres,SSE = find_split(features.T,r)
        df.loc[idx]  =[idx,thres,SSE]

    parent_sse = np.sum((r - r.mean())**2)

    min_SSE_idx = df["SSE"].argmin()
    sse = df["SSE"][min_SSE_idx]
    thres = df["thres"][min_SSE_idx]
    f_idx = df["idx"][min_SSE_idx].astype(int)
    if(np.isinf(sse)):
        return dt_node(
                    threshold=0,
                    feature=None,
                    is_leaf=True,
                    prediction=np.mean(r)
                )
    if (parent_sse <= sse):
        dt = dt_node(is_leaf=True, prediction= np.mean(r))
        return dt
    mask = X[:,f_idx] <= thres
    left_X = X[mask]
    left_r = r[mask]
    right_X = X[~mask]
    right_r = r[~mask]
    dt = dt_node(threshold = thres , 
                f_idx = f_idx , 
                left_node=create_tree(left_X,left_r,max_depth = (max_depth-1)) , 
                right_node = create_tree(right_X,right_r,max_depth = (max_depth-1)))
    return dt




class Gradient_boost:
    def __init__(self, initial_prediction=None , forest=None,learning_rate=0.1):
        self.initial_prediction = initial_prediction
        self.forest = forest
        self.learning_rate = learning_rate
    

    def train(self,X,Y,n_estimator,learning_rate,max_depth):
        initial_prediction ,forest = create_forest(X,Y,n_estimator=n_estimator,learning_rate=learning_rate,max_depth=max_depth)
        self.initial_prediction = initial_prediction
        self.forest = forest
        self.learning_rate = learning_rate
    def predict(self,samples):
        prediction = np.full(samples.shape[0], self.initial_prediction)
        for tree in self.forest:
            prediction += (self.learning_rate * tree.make_prediction(samples))
        
        return prediction





def create_forest(samples,target,max_depth,learning_rate = 0.1 , n_estimator=1 ):
    initial_prediction = target.mean()

    current_predicton = initial_prediction
    residuals = target - current_predicton
    
    forest = np.zeros(n_estimator,dtype=object)
    for i in range(n_estimator):
        tree = create_tree(samples,residuals,max_depth=max_depth)
        
        current_predicton =  current_predicton + ( learning_rate * tree.make_prediction(samples))

        
        residuals = target - current_predicton
        SSE = np.sum(residuals**2)

        forest[i] = tree
    return initial_prediction,forest





if __name__ =="__main__":
    model = Gradient_boost()
    model.train(X,Y,n_estimator=4,learning_rate=0.1,max_depth=8)
    prediction = model.predict(X)
    print(prediction)