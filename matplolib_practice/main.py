import matplotlib.pyplot as plt
import numpy as np

# x = np.random.randint(1,100,50)
# y = 2*x + np.random.randint(-20,20,50)

# plt.title("Graph learning")
# plt.xlabel("X-points")
# plt.ylabel("Y-label")

# plt.scatter(x , y , label="Point")
# plt.show()




####################BAR GRAPHS ####################################################

# x = ["Math","Science","English"]
# marks = [90,23,45]
# plt.title("Bar graph")
# plt.xlabel("subjects")
# plt.ylabel("marks")
# plt.bar(x , marks, width = 0.5)
# vertical bargraph
# plt.barh(x , marks)
#horizontal bargraph
# student= ["A","B","C"]
# before= [60,70,80]
# after = [75,85,95]
# x = np.arange(len(student))#position for where the bar garh should start
# plt.bar(x-0.2 ,before , width = 0.4 , label="Before")
# plt.bar(x+0.2 , after , width = 0.4 , label="After")

# plt.xticks(x,student) #shows group name instead of position
# #comparing two groups
# plt.legend()
# plt.show()


# plt.title("bar graph")
# language = ["Python","Java","C++","JavaScript"]
# Before = [100,80,60,120]
# After = [150,120,90,180]


# plt.xlabel("users")
# plt.ylabel("language")
# # plt.bar(language , users )
# x = np.arange(len(language))
# plt.barh(x - 0.2 , Before , height = 0.4, label="Before")
# plt.barh(x + 0.2 ,After , height=0.4, label="After")
# plt.yticks(x , language)
# plt.legend()




# plt.show()



################################## HISTOGRAMS #############################################

# plt.title("Histogram")

# marks = np.random.normal(50 ,15 , 1000)
# plt.hist(marks, bins=30)
# plt.show()


##################################### SUB PLOTS MULTIPLE GRAPHS #################################################


# x = np.linspace(-5,5,100)

# y1 = x**2
# y2 = x**3


# plt.subplot(2,2,1)
# plt.plot(x,y1)
# plt.title("y = x^2")

# plt.subplot(2,2,2)
# plt.plot(x , y2)
# plt.title("y = x^3")



# plt.show()

################### figure , axes and ##############################################

# fig , ax = plt.subplots(1,3)

# x = np.linspace(-5,6,100)
# y1 = x**2
# y2 = x**3
# ax[0].plot(x, y1)
# ax[0].set_title("Square")


# ax[1].plot(x, y2)
# ax[1].set_title("cube")


# ax[2].plot(x , np.sin(x))

# plt.show()


############################################## MATH MATICAL FUNCTIONS ########################################################################


# x = np.linspace(-2*np.pi , 2*np.pi , 200)
# fg ,ax = plt.subplots(2,2)

# ax[0,0].plot(x , np.sin(x))


# ax[0,1].plot(x , np.exp(x))

# x1 = np.linspace(0.1,5,10)
# ax[1,0].plot(x1, np.log(x1))
# plt.show()

############################################################ Matrix #########################################################################

# A =np.random.rand(3,3)
# print(A)

# plt.imshow(A)

# for i in range(A.shape[0]):
#     for j in range(A.shape[1]):
#         plt.text(j,i,A[i,j],
#                  ha="center",
#                  va="center")

# plt.colorbar()
# plt.show()


