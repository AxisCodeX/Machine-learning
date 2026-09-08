import pandas as pd
import numpy as np
import warnings
np.seterr(all="ignore")
warnings.filterwarnings("ignore", category=RuntimeWarning)
np.random.seed(123)



class decision_tree_node:
    def __init__(self,feature=None,threshold=0,left_node=None , right_node=None ,is_leaf = False ,prediction = None ):
        self.feature = feature
        self.threshold = threshold
        self.left_node = left_node
        self.right_node = right_node
        self.is_leaf = is_leaf
        self.prediction = prediction
    



    def print_tree(self, depth=0, prefix="Root:"):
        indent = "    " * depth
        
        # If the node is a leaf, print the prediction
        if self.is_leaf:
            print(f"{indent}{prefix} [LEAF] Prediction: {self.prediction}")
            return

        # Print current split details for internal nodes
        print(f"{indent}{prefix} Split on Feature {self.feature} <= {self.threshold}")
        
        # Recursively traverse left and right children
        if self.left_node:
            self.left_node.print_tree(depth + 1, prefix="True -->")
        if self.right_node:
            self.right_node.print_tree( depth + 1, prefix="False ->")


    def make_prediction(self,target):
        def predict(node,row):
            print("row : ", row)
            if node.is_leaf:
                return node.prediction
            if row[node.feature] <= node.threshold:
                return predict(node.left_node , row)
            else:
                return predict(node.right_node ,row)
        predictions = target.apply(lambda row : predict(self,row),axis = 1)
        return predictions
        



def bootstrap_sampler(X,Y):
    indices = np.random.choice(
        X.shape[0] , X.shape[0] , replace = True
    )
    X = X[indices , : ]
    Y = Y[indices]
    return X, Y



def random_feature_selection(X , max_features):
    idx = np.random.choice(
        len(np.arange(0,len(X))),
        size = max_features,
        replace=False
    )
    features =pd.DataFrame({
        "idx" : idx,
        "features" : X[idx]
    })
    return features


def split_node(X,Y):     
            unique = np.unique(X)
            if len(unique) <= 1:
                return 0,np.inf
            if np.array_equal(unique, np.array([0,1])):
                thres = np.array([0.5])
            else:
                new_x = np.sort(X)
                thres =( new_x[1:] + new_x[:-1])/2
            mask = X <= thres[: , None]
            left = np.where(mask , Y , np.nan)
            right = np.where((~mask),Y,np.nan)
            
            left_mean = np.nanmean(left,axis=1)
            right_mean = np.nanmean(right , axis = 1)

            left_sse = np.nansum((left - left_mean[:, None])**2, axis=1)
            right_sse = np.nansum((right - right_mean[:, None])**2, axis=1)

            split_sse = left_sse + right_sse
            thres_idx = split_sse.argmin()
            thres = thres[thres_idx]
            min_sse = split_sse[thres_idx]
            return thres , min_sse
            
    

def create_node(observations,predictions,f_cols):
    if(np.all(predictions == predictions[0])):
        return decision_tree_node(
                    threshold=0,
                    feature=None,
                    is_leaf=True,
                    prediction= predictions[0]
                )
    random_features = random_feature_selection(f_cols,max_features=2)
    sample = observations[: , random_features.idx]
    df = pd.DataFrame(columns=["idx","feature","thres","min_sse"])

    for idx,col_data in enumerate(sample.T):
        if(len(col_data) <= 1):
            return decision_tree_node(
                    threshold=0,
                    feature=None,
                    is_leaf=True,
                    prediction=np.mean(predictions)
                )
        thres,min_sse = split_node(col_data , predictions)
        df.loc[idx] = [idx , random_features.features[idx] , thres , min_sse]

    min_sse_idx = df["min_sse"].argmin()
    min_sse = df["min_sse"].min()
    if(np.isinf(min_sse)):
        return decision_tree_node(
                    threshold=0,
                    feature=None,
                    is_leaf=True,
                    prediction=np.mean(predictions)
                )
    thres = df["thres"][min_sse_idx] 
    f = df["feature"][min_sse_idx]
    mask = sample[: , min_sse_idx] <= thres
    parent_sse = np.sum((predictions - predictions.mean())**2)

    
    if (parent_sse  <= min_sse) :
        return decision_tree_node(
                    threshold=0,
                    feature=None,
                    is_leaf=True,
                    prediction=np.mean(predictions)
                )
    left_x = observations[mask]
    left_y = predictions[mask]
    right_x = observations[~mask]
    right_y = predictions[~mask]
    
    return decision_tree_node(
        threshold=thres,
        feature=f,
        left_node= create_node(left_x,left_y,f_cols=f_cols),
        right_node= create_node(right_x,right_y,f_cols=f_cols)
        
    )
        


    






def create_tree(features , target,n_estimator=1):
    forest = []
    for i in range(n_estimator):
        X,Y = bootstrap_sampler(features.to_numpy() , target.to_numpy())
        node = create_node(X,Y,features.columns)
        forest.append(node)
    return forest


data = {
    "area": [
        55, 60, 65, 70, 75,
        80, 85, 90, 95, 100,
        105, 110, 115, 120, 125,
        130, 135, 140, 145, 150
    ],

    "age": [
        25, 20, 30, 15, 18,
        12, 20, 10, 15, 8,
        12, 5, 10, 6, 8,
        4, 7, 3, 5, 2
    ],

    "distance": [
        12, 10, 11, 8, 9,
        7, 8, 6, 7, 5,
        6, 4, 5, 4, 3,
        4, 2, 3, 2, 1
    ],

    "price": [
        42, 47, 45, 55, 58,
        64, 62, 72, 70, 78,
        81, 90, 87, 96, 101,
        108, 111, 120, 124, 132
    ]
}

df = pd.DataFrame(data)
X = df.iloc[: , :3] # 20 samples 3 features
Y = df.iloc[: , -1]

test_data = pd.DataFrame({
    "area":     [65, 85, 100, 120, 140, 150, 72, 108],
    "age":      [22, 15, 10, 5, 3, 1, 17, 8],
    "distance": [9, 7, 5, 4, 2, 1, 8, 5],
    "price":    [50, 65, 78, 94, 115, 132, 58, 84]
})
test_x = test_data.iloc[: , :3]
if __name__ == "__main__":
    forest = create_tree(X,Y,3)
    print(forest)
