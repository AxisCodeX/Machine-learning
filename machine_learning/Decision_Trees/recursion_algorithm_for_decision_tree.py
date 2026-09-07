import numpy as np

X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
Y = np.array([0, 0, 1, 0, 1, 1, 0, 1])


class decision_tree:
    def __init__(self,thres,Gini,left_node,right_node,X,Y,is_leaf=False,Gini_gain=0,prediction_class = None):
        self.thres = thres
        self.Gini = Gini
        self.Gini_gain = Gini_gain
        self.X = X
        self.left_node = left_node
        self.right_node = right_node
        self.is_leaf = is_leaf
        self.prediction_class = prediction_class


def split_node(X , Y):
    n = len(Y)
    class0 = np.sum(Y==0)
    class1 = np.sum(Y==1)
    P_0 = class0/n
    P_1 = class1/n
    Gini_parent = 1 - (P_0**2 + P_1**2)
    unique,counts = np.unique(Y , return_counts = True)
    if n==1 :
        dt = decision_tree(thres = X[0],Gini=Gini_parent,left_node=None,right_node=None,X=X,Y=Y,is_leaf=True,prediction_class=Y[0])                                  
        # print(dt.__dict__)
        return dt
    elif len(unique) ==1:
        dt = decision_tree(thres = X[0],Gini=Gini_parent,left_node=None,right_node=None,X=X,Y=Y,is_leaf=True,prediction_class=unique[0])
        # print(dt.__dict__)
        return dt



    thres =( X[1: ] + X[:-1])/2
    mask = X < thres[: , None]
    left_count = mask.sum(axis = 1)
    right_count = np.sum(~mask , 1)
    
    left_class1 = (Y * mask).sum(axis = 1)
    left_class0 = left_count - left_class1


    right_class1 = (Y * ~mask).sum(axis = 1)
    right_class0 = (right_count - right_class1)



    Gini_left = 1 - ((left_class0/left_count)**2 + (left_class1/left_count)**2)
    Gini_right = 1 - ((right_class0/right_count)**2 + (right_class1 / right_count)**2)

    Gini = 1/n * (left_count*Gini_left + right_count* Gini_right)
    min_thres = Gini.argmin()
    Gini_gain = Gini_parent - Gini[min_thres]

    split_index = min_thres +1
    left_node_x = X[:split_index]
    right_node_x = X[split_index :]

    left_node_y = Y[: split_index]
    right_node_y = Y[split_index:]


    if(Gini_gain <= 0.01):
        dt =  decision_tree(thres =thres[min_thres] ,Gini=Gini[min_thres] , Gini_gain=Gini_gain,left_node=None,right_node=None,X=X,Y=Y,is_leaf=True,prediction_class=0 if class0 >class1 else 1)  
        # print(dt.__dict__)
        return dt
    

    dt = decision_tree(thres =thres[min_thres],Gini= Gini[min_thres],Gini_gain=Gini_gain,right_node=split_node(right_node_x,right_node_y),left_node=split_node(left_node_x, left_node_y),X=X,Y=Y)
    # print(dt.__dict__)
    return dt


def predict_class(dt,x):
    if (dt.is_leaf):
        prediction = dt.prediction_class
        return prediction
    if(x < dt.thres):
        prediction = predict_class(dt.left_node,x)
        return prediction
    else:
        prediction = predict_class(dt.right_node,x)
        return prediction








if __name__ =='__main__':
   d_t =  split_node(X,Y)
   print("\n\n\n")
   prediction = predict_class(d_t , 8)
   print("\n\n\n")
   print("prediction : ", prediction)
