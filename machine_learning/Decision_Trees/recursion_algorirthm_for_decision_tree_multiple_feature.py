import numpy as np
import pandas as pd
import multiprocessing


df = pd.DataFrame({
    "score": [
        10, 20, 30, 40,
        50, 60, 70, 80,
        90, 100, 110, 120,
        130, 140, 150, 160
    ],

    "experience": [
        1, 1, 2, 2,
        3, 3, 4, 4,
        5, 5, 6, 6,
        7, 7, 8, 8
    ],

    "attendance": [
        0, 1, 0, 1,
        0, 1, 0, 1,
        0, 1, 0, 1,
        0, 1, 0, 1
    ],

    "target": [
        0, 0, 0, 1,
        0, 1, 1, 1,
        0, 1, 1, 1,
        0, 1, 1, 1
    ]
})



X = df.iloc[: , :3]
Y = df.iloc[:,-1]

class decision_tree_node:
    def __init__(self,feature,threshold,Gini = 0 , Gini_gain = 0 ,X = None , Y= None ,left_node = None , right_node = None , is_leaf = False,prediction=None):
        self.feature = feature
        self.threshold = threshold
        self.Gini = Gini
        self.Gini_gain = Gini_gain
        self.left_node = left_node
        self.right_node = right_node
        self.is_leaf = is_leaf
        self.prediction = prediction
        self.X = X
        self.Y = Y
    
    def print_tree(self, depth=0, prefix="Root:"):
        indent = "    " * depth
        
        # If the node is a leaf, print the prediction
        if self.is_leaf:
            print(f"{indent}{prefix} [LEAF] Prediction: {self.prediction} (Gini: {self.Gini:.4f})")
            return

        # Print current split details for internal nodes
        print(f"{indent}{prefix} Split on Feature {self.feature} <= {self.threshold} "
            f"(Gini: {self.Gini:.4f}, Gain: {self.Gini_gain:.4f})")
        
        # Recursively traverse left and right children
        if self.left_node:
            self.left_node.print_tree(depth + 1, prefix="True -->")
        if self.right_node:
            self.right_node.print_tree( depth + 1, prefix="False ->")

    def predict(self , target):
        def make_prediction(dt,row=0):
            if dt.is_leaf:
                return dt.prediction
            
            if row[dt.feature] < dt.threshold:
                return make_prediction(dt.left_node,row)
            else:
                return make_prediction(dt.right_node , row)
        target["prediction"] = target.apply(lambda row : make_prediction(self , row), axis = 1)
        return target["prediction"]



def find_thres(X,Y):
    n = len(Y)
    unique = np.unique(X)
    if np.array_equal(unique,[0,1]):
        thres = np.array([0.5])
    else:
        new_x = np.sort(X)
        thres = (new_x[1: ] + new_x[:-1])/2
    
    mask = X < thres[: , None]
    
    left_count = np.sum(mask , axis = 1)
    right_count = np.sum(~mask, axis = 1)

    left_class1  = (mask * Y).sum(axis = 1)
    left_class0 = left_count - left_class1

    right_class1 = (~mask * Y).sum(axis = 1)
    right_class0 = right_count - right_class1
    with np.errstate(invalid="ignore"):
        Gini_left = 1 - ((left_class0/left_count)**2 + (left_class1/left_count)**2)
    Gini_right = 1 - ((right_class0/right_count)**2 + (right_class1/right_count)**2)
    
    Gini = 1/n * (left_count * Gini_left  + right_count * Gini_right)
    Gini = np.where((left_count==0 )| (right_count ==0) , np.inf , Gini)

    thres_idx = Gini.argmin()
    thres  = thres[thres_idx]
    Gini = Gini[thres_idx]
    return thres_idx , thres , Gini

def create_decision_tree(features,target):
    def split_node(X,Y):
        df = pd.DataFrame(columns=['idx', 'thres', 'Gini'])
        for idx,col_data in enumerate(X.T):
            n = len(X)
            unique = np.unique(Y)
            if len(unique) == 1:
                dt = decision_tree_node(feature=None , threshold=None , Gini=0 , Gini_gain=0 ,left_node=None ,right_node=None,X= X , Y=Y, is_leaf = True , prediction = unique[0])
                return dt
            if n == 1:
                dt =  decision_tree_node(feature=None , threshold=None , Gini=0 , Gini_gain=0 ,X=X ,Y=Y,left_node=None ,right_node=None, is_leaf = True , prediction = Y[0])
                return dt
            thres_idx ,thres,Gini = find_thres(col_data,Y)
            df.loc[idx] = [idx, thres, Gini]
        n = len(Y)
        class0 = np.sum(Y==0 )
        class1 = np.sum(Y==1)
        Gini_parent = 1 - ((class0/n)**2 + (class1/n)**2)
        Gini = df['Gini'].to_numpy().min()
        Gini_gain = Gini_parent - Gini
        if Gini_gain < 0.01:
            dt =  decision_tree_node(feature=None , threshold=None , Gini=Gini_parent ,X=X,Y=Y, Gini_gain=0 ,left_node=None ,right_node=None, is_leaf = True , prediction = 0 if class0 > class1 else 1)
            return dt
        idx = df['Gini'].to_numpy().argmin()
        thres = df['thres'][idx]
        mask  = X.T[idx] < thres
        left_X = X[mask]
        left_Y = Y[mask]
        right_X = X[~mask]
        right_Y = Y[~mask]
        dt =  decision_tree_node(feature=features.columns[idx],threshold=thres , Gini=Gini ,X=X , Y=Y ,Gini_gain=Gini_gain ,left_node=split_node(left_X,left_Y) ,right_node=split_node(right_X,right_Y))
        return dt
    dt = split_node(features.to_numpy(),target.to_numpy())
    return dt


def calc_gini(node):
    n = len(node.Y)
    class0 = np.sum(node.Y ==0)
    class1 = np.sum(node.Y ==1)
    p0 = class0/n
    p1 = class1/n
    Gini = 1 - (p0**2 + p1**2)
    return Gini,n



def post_prune(root , alpha):
    def prune(node):
        n = len(node.Y)
        if node.is_leaf:
            gini_leaf,n = calc_gini(node)
            risk = n*gini_leaf
            
            return risk,1
        
        left_risk , left_no_of_leaves = prune(node.left_node)
        right_risk ,right_no_of_leaves= prune(node.right_node)
    
        gini,n = calc_gini(node)
        no_of_leaves = left_no_of_leaves + right_no_of_leaves
        risk = (gini * n)
        purned_cost = risk  + alpha
        not_purned_cost = (left_risk + right_risk) + alpha*(no_of_leaves)

        if purned_cost <= not_purned_cost:
            class0 = np.sum(node.Y == 0)
            class1 = np.sum(node.Y ==1)
            node.is_leaf = True
            node.prediction = 0 if class0 >class1 else 1
            node.left_node = None
            node.right_node = None
            return risk,(1)
        
        return (left_risk + right_risk) ,(no_of_leaves)
    prune(root)
        








# df_test = pd.DataFrame({
#     "score": [
#         15,   # Unseen score (between 10 and 20)
#         35,   # Edge case near an expected positive target
#         5,    # Out of bounds (lower than training minimum)
#         170,  # Out of bounds (higher than training maximum)
#         60,   # Exact match from training (Expected: 1)
#         130,  # Exact match from training (Expected: 0)
#         75,   # Unseen score with high experience
#         25    # Low score, mid experience
#     ],

#     "experience": [
#         1,    # Low experience
#         2,    # Low experience boundary
#         0,    # Zero experience (edge case)
#         9,    # High experience (edge case)
#         3,    # Exact match row
#         7,    # Exact match row
#         4,    # Mid experience
#         3     # Mixed combination
#     ],

#     "attendance": [
#         0, 1, 0, 1, 1, 0, 0, 1
#     ],

#     # Ground truth labels for you to validate your predictions against
#     "expected_target": [
#         0, 1, 0, 1, 1, 0, 1, 0
#     ]
# })


if __name__ =="__main__":
    decision_tree = create_decision_tree(X,Y)
    # prediction = decision_tree.predict(df_test)
    # print("print_prediction class : ",prediction)
    post_prune(decision_tree , 1)
    decision_tree.print_tree()


#for larger alpha value in post purning the model decides that the improvement in impurity from keeping all these split isnt worth paying the complexty penalty for all those leaves