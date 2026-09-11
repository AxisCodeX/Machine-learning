ok back to Ada boosting , i need to ask few question , i went ahead and looked read ada boosting a little bit i got to learn that 

Ada bosting uses sample weights initially every sample gets same sample weight so each obervation is equally important 

then we create a stump using Gini impurity or entropy 

then we use this stump( a classifier) on the same data set and see how many sample it fails to correctly classify 

then we calculate its total error someting like classifier_total_error = sum of sample weight of incoorectly clasified sample 

then we use this total error to calculate amount of say or we can say this as how amount of how much influence it will have in the final overall prediction 
if total_error is close to 1 i.e this classifer almost incorreclty classifed all the samples it will get a lower amount of say or a negative meaning this classfier is so bad it will negatively influence our final prediction 

if total_error is close to 0.5 meaning the classifier did no better job than guessing each class then it will get a amount of say of 0 meaning this classfier is no good so we will not let it influence our final prediction 

and if ottal error is close to 0 , this means our stump is very good at correctly classifying every sample so it will get a higher positive value of amount of say , that means this classifier is so good we should consider its prediction much more for our final prediction


and in next step we increase the smaple weight of each incorrectly classified sample on the basiss of stump's amount of say 
so if the amount of say is high that means even tho the stump is extremely good at classifying the data it still made this error so this sample must be extremely hard so it wil increase its sample weight by bigger value

similarly if the amount of say is low that means the stump was bad at predicting class so we should not focus on the mistake it made for our new stump  , so it will increase its sample weight by very small value 

similarly we also decrese the sample weight of the samples that were correctly classified , again on the basis of amount of say , if the amount of say is high that mean the model was very good , we will decrese the sample weight by less value 

and if the amount of say is less then the model was already bad at predicting every value so we should not be dependent on its prediction so it will decrese the sample weight by a larger value 

overall this process makes it easy for our next weak learner to know which sample is harder or which sample is costly if made incoorect prediction on it 

but how does it imporve on this imformation ?
with our new sample weight 
we will again create a stump -> lets class it a clasifier again

this we will use this classifier on the sample dataset , and calculate its error
and if it made the same error as the previous one it will get high total_error and less amount of say 

and if it corrected the error of the previous classifier then it wil get less total_erroor and higher amount of say 


so looking at thie process each classifier get a amount of say or influence on the final decision , but the new classifer necessearly did not improve , we just saw if it improve we will consider its prediction more and if it hasnt improved we wil consider its prediction less important

even after incresing the sample weight our next weak learner can make the same mistake , so there is no improve ment we only assige a amount of say based on it it improved or not but there is no gaurantee that it will improve 



# Yes — and your reasoning is mostly correct. In fact, you've identified the most important conceptual question about AdaBoost:

# “We increased the weight of hard samples, but what guarantees that the next stump actually becomes better?”

# The answer is: there is no guarantee that it will fix every previous mistake. And that's okay