# import numpy as np
# import matplotlib.pyplot as plt
# import math



# p = 0.6 
# outcomes = ["P","1-P"]
# plt.xlabel("Random variable X")
# plt.ylabel("Probablity")
# plt.title("Bernoulli PMF")
# plt.ylim(0,1)
# plt.grid(axis ="y",alpha= 0.3)
# plt.bar(outcomes,[p,1-p], 0.5)
# plt.show()



# x = np.random.normal(170, 10 , 1000)
# plt.title("normal distribution ")
# plt.xlabel("Heights")
# plt.ylabel("Frequency")
# plt.hist(x, bins=10)
# plt.grid(True , alpha= 0.7)
# plt.show()



## theoritical construction of binomial distribution

# def find_probablity(n,p,r):
#     C = math.comb(n,r)
#     pro= C * math.pow(p, r) * math.pow( ( 1- p) , ( n - r ))
#     return pro


# Bins = np.vectorize(find_probablity)
# n= 10
# x = np.random.randint(0,2,n)
# p = np.sum(x)/n
# r = np.arange(0,11)
# y = Bins(10 , p , r)
# print(y)
# plt.title("Binomial distribution ")
# plt.xlabel("Success")
# plt.ylabel("Probablity")
# plt.bar(r , y  )
# plt.show()



# n = 10
# no_of_simulation = 10000
# x = np.random.randint(0,2,(no_of_simulation,n))

# Y = np.sum(x , axis = 1)

# values , count= np.unique(Y , return_counts=True)
# print(values)
# print(count)

# probablity = count/no_of_simulation

# plt.bar(values , probablity )
# plt.xlabel("X = no of heads")

# plt.ylabel("Probablity")
# plt.title("Binomial Distribution")
# plt.grid(True)
# plt.ylim(0,np.max(probablity)*1.05)
# print(np.sum(probablity))
# plt.show()
# print()



# plt.quiver(
#     0,0,
#     3,2,
#     angles = 'xy',
#     scale_units = "xy",
#     scale = 1
# )
# # colors = np.random.rand(100)
# # x = np.linspace(-5,5,100)
# # y = 2*x
# # plt.scatter(x, y, c=colors, cmap="viridis")
# plt.grid()
# plt.ylim(-1,5)
# plt.xlim(-1,5)
# plt.show()






####EXPERIMENT #############################################################################################



################# THEORITHICAL BINOMIAL DISTRIBUTION V/S SIMULATION OF BINOMIAL DISTRIBUTION #########################################

# import numpy as np
# import matplotlib.pyplot as plt
# import math 


# n = 10
# p = 0.5
# X = np.arange(0,11)


# def prob(n , p , x):
#     C = math.comb(n, x)
#     prob = C * (math.pow(p , x)) * (math.pow((1-p),n-x))
#     return prob


# calc_probablity = np.vectorize(prob)


# fig , ax = plt.subplots(1,2)
# probablities = calc_probablity(n,p,X)
# ax[0].set_title("Theorithical histogram of binomial distribution")
# ax[0].set_ylabel("Probablities")
# ax[0].set_xlabel("X  = No of success")
# ax[0].bar(X , probablities , 0.8)
# ax[0].set_ylim(0 , probablities.max() * 1.05)



# no_of_experiment = 100
# Y  = np.random.randint(0,2,(no_of_experiment,n))
# Z = np.sum(Y , axis = 1)
# values , count = np.unique(Z , return_counts = True)

# sim_probablities = count/no_of_experiment

# ax[1].set_title(f"Simulation of a binomial experiment (N= {no_of_experiment})")

# ax[1].set_ylabel("Probablities")
# ax[1].set_xlabel("X = No of success")
# ax[1].bar(values , sim_probablities , 0.8)
# ax[1].set_ylim(0,sim_probablities.max()*1.05)





################################# SIMULATION OF SAMPLING #################################################################################

# import numpy as np
# import matplotlib.pyplot as plt
# import math
# np.random.seed(1234)

# fg , ax = plt.subplots(1,2)

# data  = np.random.normal(170 , 10 , 10000)
# mean = 170
# std = 10

# ax[0].hist(data, bins =  20)
# ax[0].axvline(x = mean,color = "red")
# ax[0].set_title("Normal Distribution (POPULATION)")
# ax[0].set_ylabel("Frequency")
# ax[0].set_xlabel("Heights")



# #### sampling ###############################################

# n = 100
# no_of_experiment = 10000

# samples= np.random.choice(data,(no_of_experiment , n))
# sample_means = np.mean(samples , axis = 1)

# estimated_mean = np.mean(sample_means)
# print(estimated_mean)
# std_error = std/math.sqrt(n)
# print(std_error)


# ax[1].hist(sample_means , 30)
# ax[1].set_title("Sampling")
# ax[1].set_ylabel("Frequency")
# ax[1].set_xlabel("Sample_Means")
# ax[1].axvline(x = np.mean(sample_means) , color="red")


###################################### Simulating Biased events  ########################################################################################

# import numpy as np
# import matplotlib.pyplot as plt
# import math 





# p = 0.7
# n = 11
# def pmf(n , p , x):
#     C = math.comb(n,x)
#     prob = C * math.pow(p , x) * math.pow(1-p,n-x)
#     return prob

# find_probablities = np.vectorize(pmf)

# X = np.arange(0,11)

# probablities = find_probablities(n , p , X)

# fig , ax = plt.subplots(1,2)
# ax[0].bar(X,probablities, 0.8)
# ax[0].set_title("Theoritical biased binomial distribution")
# ax[0].set_xlabel("X = no of successes")
# ax[0].set_ylabel("Probablities")
# ax[0].set_ylim(0, np.max(probablities) * 1.05)






# no_of_experiment = 1000
# n= 11


# X = np.random.choice(
#     [1,0],
#     size=(no_of_experiment,n),
#     p=[0.7 , 0.3]
# )
# print("Heads : ", np.sum(X == 1))
# print("Tails : ", np.sum(X == 0))
# Y = np.sum(X , axis = 1)

# values , count = np.unique(Y , return_counts=True)
# sim_probablities = count/no_of_experiment
# print("Probablities", sim_probablities)
# print("values : ", values)
# print("count : ",count)
# ax[1].set_title("Simulation of biased binomial distribution")
# ax[1].set_xlabel("X = no of success")
# ax[1].set_ylabel("Probablities")
# ax[1].set_ylim(0 , sim_probablities.max() * 1.05)
# ax[1].bar(values , sim_probablities , 0.8)


# plt.show()


####################### simulation of skewed data ##########################################################################################





# import numpy as np
# import matplotlib.pyplot as plt
# import math 


 


# data = np.random.lognormal(mean = 2 , sigma = 0.5 , size = 10000)
# # data = -np.random.lognormal(mean = 2 , sigma = 0.5 , size = 10000)for left skewed

# population_mean = data.mean()
# population_std = data.std()


# fig , ax = plt.subplots(1,2)
# ax[0].hist(data, bins = 100)
# ax[0].set_title("Right skewed data")
# ax[0].set_ylabel("Frequency")
# ax[0].set_xlabel("Values")
# ax[0].axvline(x = population_mean, color = "red")


# ### sampling

# no_of_experiment = 1000
# n = 100
# samples = np.random.choice(data , size=(no_of_experiment, n))

# sample_mean = np.mean(samples , axis= 1)

# estimated_mean = sample_mean.mean()
# std_error = population_std / math.sqrt(n)


# ax[1].hist(sample_mean , bins = 30)
# ax[1].set_title("Sampling")
# ax[1].set_ylabel("Frequency")
# ax[1].set_xlabel("Values")
# ax[1].axvline(x = estimated_mean)
# plt.show()
# print("population_mean : ", population_mean)
# print("population_std : ", population_std )
# print("estimated_mean : ", estimated_mean)
# print("std_error : ", std_error)
# plt.show()



