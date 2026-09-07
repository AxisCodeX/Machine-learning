import numpy as np






A) => the model B with training R^2 = 0.99  but test R^2 only 0.45 is overfitting  as it did so well in the trainig set but not so much goog in the test set

B)=>  The model C with traiining R^2 = 0.55 and testing R^2 = 0.52 is underfititng the model may be just to osimple to understand the underlaying relation ship etween the dependent and independent variables, so it has high bias but low variance as it performed equally bad in both test and train set

c) for deployment model A with Training R^2 = 0.72 and test R^2 = 0.70 is best as it did not perform overaly bad in both test and traing set , so i would say amoung the presented model model A has generalized better than other

D) model B has low bias and high variance , one of its cause might be model being to complex , having large weight , regularization will draw a boundary and force it to settle with a relatively lower weight + low loss 



A) if we have lambda = 5 then the pendalty added to the objective is  (100 + 4 + 64) * 5 = 168 * 5  = 840 this is very high penalty it might cause the model to eventually underfi

B) with respect to w1 the gradient pentlaty will be 2*rigigd_strength*w1

c) with respect to w3 = -8 the gradient penalty is 2*5*-8 = -80


D)even though the gradient itself if negative (-8) the L2 penalty will push it toward zero as L2 regulariation does not care about direction of weight it esential only cares abot keeping the magnitude of weight close to 0

E)no ridge regularization does not make the weight exactly zero as it used squared weiight whose graidnet penatly becomes 2*lambda*w so as w aproaches 0 the ridge force essentialy dissapers but with L1 there is a constant force being applies at either side of 0 so even if w approaches zero the force will still remail +1 for w >0 and -1 for w<0 only at zero using subgradiant we make force = 0 so it can make weight clcose to 0 until it becomes 0 




w = 0.1
r_s = 1

g(BCE) = -0.05
lr= 1


for L1 
gradient pentaly = rs* sign(w) = 1 * 1 = 1
so overall gradient(dw) = -0.05 + 1 = 0.05

w_new = w - lr*dw = 0.1 - 1*(0.05) = 0.1 - 0.05 = 0.05


for L2
gradient penalty = 2 * rs * dw = 2 * 1 *0.1 = 0.2

overall_gradient (dw) = -0.05  + 0.2 = 0.15

w_new = w - lr*dw = 0.1 - 0.15 = -0.05


so ridge regulariztion shrinks w more in this  particular step here L1 reduces 0.05 but L2 reduces 0.15 

with w = -0.1 the L1 penalty will try to increase it , or move to ward zero as the sign(w) will produce -1 and in updationg step we wil get  -0.1 + 0.05 





## logistic regression 

OLR is a poor choice because , the OLR is used to predict continuous value which can go -infinity to positive infinity which we could not interpret as probablity which is required for classification problem so we need somethign that can output in probablity scale

for example if we are clasificing disease A and diesee B based on hearbeed , bp and other LR can predict 20 , 30 or even in negative scale which woul be hard to clasify based on 

sigmoid function solves the problem which was limiting linear regresison from being used in classification problem , ie its prediction can go to infinity abd beyond , sigmoid function takes the linear predictor from linear regresison can converts it into probablity 

sigmoid function always produces value from 0 to 1

logistic regression is producing a probablity for a observation based on the feature and then we use a threshold 0.5 , if p >0.5 we classifuy it one class and if it is <0.5 we classify it with another class 




#sigmoid and log odd

if z = 0 then p = 0.05 then if z >0 then p>0.5 and z<0 then p<0.5

z  = 0 corresponds to the decision boundary when the thress hold = 0.5

p/1-p represents the odds of blonging to  a class because form this formual we can calculate proablbltiy


#BCE 

for y = 1 and p = 0.9
the BCE = -log(0.9)

for y = 1 and p = 0.1
the BCE = -log(0.1)

the BCE is for y = 1 log(p) if we take the drivative we get 1/p so if p is close to 1 we get less penalty but if it is far from actual classification then we get larger penalty same goes for log(1 - p)




for correct class if the proabblity is predicted extremely close to 0 then BCE increases 





#

the term (p - y) appears in the gradient because that term is essentialy what is calculating how off our current prediction is  , and we move our parameter accurning to that term

also while derivating the loss with respect to w from chain rule dl/dp * dp/dz * dz*dw  that terms appears naturally


if y = 1 and p = 0.8 . p - y wil have -ev sign  so the gradient descent should increase w , wel we stil cant confidently say that because the actally gradient descent term also includes xi and it could change the direction 

if y = 0 and p = 0.2 then p-y will have +ev sign so it should decrease w assuming the curent feature value is also positive

# Decision boundary
z=2*x1 ​−3*x2​ +6

the equation that defines the decision boundary is (z - 2x1 -6)/-3 = x2​

the slope tells us ith increase in x1 by unit 1  the feature x2 tends to increase by 2 units

the classification thershold  is what we choose to determine how strong our prediction should be for it to achieverclass 1 so the actaually decision boundary is stil given by the eqn above
for multiple feature the decsion boundary efffectly becomes a hyperplane




#feature scaling

different feature scale can cause problem beacuse of their units being different for example to predict if a house if expensive or not we can look  at its area and age the area could be enourmous like 5000 but the age can be only 50 -60 well the area will affect it heavily giving less improtance to age which in practicle sense is more important , and i know this is not a good example but it clears the problem

b if one feature has value 1000 whie another has values 0.1 die to x1 bing 1000 it will pull mostly control in which direciton the weight should increase , almost neglecting 0.1 which could be equally important 


  i used standarization (x-x.mean)/s.std

after standarization the mean is 0 while the std is around 1


standarization does changes the information contained in the feature , after that all feature can get equall chance on contributing to gradient descent  , after standarization we can only talk about change in std unit and not their original unit , also since all the feature wil be in same scale , it wil be easy to compare and see which one s use full and which one is not




A) in MSE we calculate residuals , which are the distance from the predicted point to the actuall point , logistic regression does not have those residual in the same sense as linear regression, if we converted the probablity scale of logistic regresison in to log odd scale wee wouldsee that every point lies in the infinity and the residuals are just infinity so we cant use the regular MSE as there is no residuals

B) THe major advantage of BCE is that is penalizes more when the model is confidently incorrect and less when it is close to actua data



C) sigmoid converts the linear score of z into probablity before BCE is calculated

D) gradient particular look at the error along with the feature value for figuring out which direction it should push w that why p-y appears in the derivation of gradient from loss function
the chain rule looks like this dl/dp * dp/dz * dz/dw 






A)
 for linear regression multi collinearity is a problem because multicolinearity makes it hard to determine the individual effect of the feature on the prediciton , so many combination of weights can produce the same prediction that is the real problem 
B) no the model cannot seperate and calculate the individial effect of w1 and w2 

C) when the feature are perfectly linearly depedent the determentant of i believe XTX becomes somewahat a skew matrix and simgilar matrix so the inverse does not exist

D) no multicollinearity does not necesarily mean the models prediction wil be terrible it jusst means , some weight might be heavily larger than other , and other receive lowere weight 
a heavy multicolinearty means some feature are not contributing that much and removing that might increase computational efficency and models complexity


E) ridge regresison will prevent weights from getting a lot larger by adding heavy penalty to larer weight so the model will settle will relatively a litter more loss but lower weight value 





A ) we usually regularize te weights but not bias because the bias is the predicted value when all the feature are 0 , and bias needs fredom inorder for the cirve to fit the data best , also the penalty term naturally does not arrive into the derivation of bias gradient

B)the l2 penalty is  2*rs * (w1 + w2 ) = 2*rs * (10 - 8) = 4 * 2 = 8


c for w1 and w2 the regularization gradient penalty is 1/n SUM( p - y) +2 * rs SUM (w)  40 and -32 respectively


D)  the regularization gradient for b is  1/n SUM( p - y) 

E) if we regularized the b ias just like the weights the model will limit the value of bias also which might make it difficult to predict correct value instead of making it better, it will unnecessarly restric where the decision boundary will appear





A) the L1 penalty is 1 * (5 + 0.2 - 3 + 0) = 2.2

B for w >0 the L1 regularization is rs * 1 = rs = 1

C)  for w <0 the L1 regularization is 1 * -1 = -1

D) In L2 when the weight starts to get realy close to zero the force becomes expreemlty small so it ususlly does nt pull any feature exactly to zero , but for L1 untill the feature is >0 or <0 there will be a constant force of either -1 or +1 weighted by r_s  so it can pull weights to exactly zero

E) if w = 0.01 and gbce = 0.005 and rs = 1 , lr = 0.01 then 

overall all gradient (dw) = 0.005 + 1 * 1 = 1.005

w = w - lr*dw = 0.01 -  0.01 * 1.05 = -0.00005






1) for ordinary linear regression there is a closed form solution ,
lniear regression + gradient descent there is no closed form so;lution the greadient descent it self is a optimization method which produces values close to true theoritical value 
ridge regresioon for linear regression + L2 regularization there is a closed form solution  but for logistic regression there is not a closed form soltion
logistic regression  there is no closed form solution we used variaous optmization method(usually gradient descent )



A) logistic regresison fundamentally requires an iterative optimization method like gradient descent

B) because in logisc tic regression we arent directly working with w and b in the BCE we are woring with probablity so if we try to find a normal euqation with the BCE it beecomes much more complicated

C) NO adding L2 reguilarization only restrics its wieght form getting realy big it does not automatically give a closed form solution 



A) we cant simply use the sigmoid becvause the sigmoid can only poduce proabalites for two class and not more than that

B) for multiclass logistic regression we use softmax function instead of sigmoid 


C) if the model produces some raw score in multiclass logistic regresison we should first convert them to likelihood by passig them through softmax functionbefore we use them for determining class

D) the resulting class probablites must add up to 1 , 

E) form the given probabilities the model predicts y = 0

A) 11.1073379274
B)P(y = 0) = 0.66524095741
P(y = 1) = 0.24472847165
P(y = 2) = 0.09003057339


they sum to 1.00000000245 so there is a precision error in the above probablity calculaiton

if z changes to [12,11, 10] then the predicted probablity changes so the model wiil try to fit accordinagly but for this the raw prediction for y = 0 is still greater than other so the model will still predict y = 0





A) softmax logistic regression predicted probablities sum up to exactly one , but the three independed binary classifiers can produce result that exceed 1 when summed they are only good for predicting between two classes


B) softmax naturally garantuess that the three predicted form one coherent probablitiy distribution because the produced probablities sum up to one 
C)the predicted class is 1


D) L = -log(P(y = 1)) = -log(0.46396342796) 


E) if th true class is 1 then the logg wil be huge as the liear predictor is favoring class 0 extremely 

F) hen y is represented as one hot vector the yk other than the actuall class becomes 0 so only yklogpk survives











