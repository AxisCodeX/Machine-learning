import numpy as np

# arr = np.array([1,3,5,7])

# print((arr.reshape(4,1) - arr).shape)


# arr = np.zeros((5,5))
# z = np.ones((5,2))
# arr[0: , [0,-1]] = z


# arr[[0,-1] , 1:-1] = np.ones((2,3))
# arr[2,2] = 9
# print(arr)


# arr = np.arange(1,31).reshape((6,5))
# print(arr)
# print(arr[2:4 ,0:2])

# print(arr[[0,1,2,3],[1,2,3,4]])
# print(arr[[0,-2,-1], 3:5])


# arr = np.arange(1,7).reshape((3,2))

# print(np.sum((arr**2),axis=1))


# image = np.zeros((100,100,3))

# image[: , : , [0]] += 1


# print(image[: , : , 0].shape)
# print(image[: , : , [0]].shape)
# print(image[: , : , 0 : 1].shape)
# print(image[: , : , [0,1]].shape)
# print(image[: , : ,1: ].shape)




# arr = np.arange(25).reshape(5,5)
# print(arr)
# print(arr[[0,1,2,3,4],[0,1,2,3,4]])



# arr =np.array([
#  [10,20,30],
#  [40,50,60],
#  [70,80,90]])


# indices = [2,0,1]

# print(arr[[0,1,2] , indices])


# #randomly reording rows
# print(arr[[2,0,1], : ])


# arr = np.random.randint(-100,100 , 20)
# print(arr[ (arr %2 == 0)   | (arr%5 == 0)])

# arr[ arr < 0 ] = 0 
# print(arr)



# arr = np. array( [
#     [
#     [1,2,3,6],
#     [4,5,6,7],
#     [7,8,9,8]
#     ],
#     [
#     [1,2,3,6],
#     [4,5,6,7],
#     [7,8,9,8]
 



# arr = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# bias = np.array([10 , 20 , 30])


# print(arr + bias)


# arr  = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# scale = np.array([1,10,100])


# print(arr * scale[: , np.newaxis])


# x = np.array([0,1,2,3])
# y = np.array([0 , 10 , 20])


# y = y[: , np.newaxis]

# print(x + y)




# image = np.random.randint(0 , 255 , (500 , 800 , 3))


# mean = np.array([123.5, 117.2, 104.8])
# std  = np.array([58.1, 57.3, 57.7])

# print((image - mean ) / std)


# x = np.random.random((1000 , 784))
# w = np.random.randint(0 , 100 , (784,))
# b = np.array([1])

# print( ((x @ w) + b).shape)


# points = np.array([
#     [1,2],
#     [4,6],
#     [7,1]
# ])

# x = points[: , np.newaxis , : ]
# y = points[np.newaxis , : , : ]

# print(x - y)


#advance indexing

# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# print( arr[[0,1,2] , [0,1,2]])


# arr = np.arange(1 , 9 ).reshape(4,2)
# print( arr[[-1 , 0 , 2] , : ])



# arr  = np.arange(1,13).reshape((3,4))
# print(arr[: , [2 , 0 , 2]])



# img = np.random.randint(0 , 256 , (100 , 100 ,3))

# rows = np.array([10 , 50 , 90])
# columns = np.array([20 , 70 , 15])

# print(img[rows, columns, :])


# arr = np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ])

# print( arr[[0,1,2,3], [0,1,2,3]])
# print(arr[[0,1,2,3] , [3,2,1,0]])


# scores = np.array([
#     [80, 75, 90],
#     [65, 88, 72],
#     [91, 85, 95],
#     [70, 60, 78]
# ])

# best_subject = np.array([2,1,2,0])

# print( scores[[0,1,2,3], best_subject])


# arr = np.arange(1,10).reshape(3,3)
# print(arr)
# (arr[[0,1], [1,2]]) # returns [2,6]
# (arr[[0,1]][:, [1,2]]) #returns [[2 3][5 6]]




##boolean masking

# arr = np.array([3, 8, 11, 14, 19, 22, 27, 30])

# mask = arr %2 == 0
# print(mask)
# print( arr[mask])
#or
# print(arr[arr %2 ==0])

# arr = np.array([
#     [ 4, -2,  7],
#     [-5,  8, -1],
#     [ 3, -9,  6]
# ])

# arr[arr < 0] = 0
# print( arr)

# scores = np.array([
#     [80, 75, 90],
#     [45, 60, 55],
#     [92, 88, 95],
#     [50, 48, 52]
# ])

# mask  = scores > 70
# print(mask)
# print(scores[scores[: , 0] > 70])


# ages = np.array([12, 17, 19, 25, 31, 65, 70])
# print(ages[(ages >= 18) & (ages < 65)])


# img = np.random.randint(0,256,(5,5),dtype=np.uint8)
# img[img >= 128] = 255
# img[img < 128 ] = 0
# print(img)



# img = np.random.randint(
#     0,256,
#     (100,100,3),
#     dtype=np.uint8
# )

# mask = (img[: ,: ,0] > 200) & (img[: ,: ,1] > 50) & (img[: ,: ,2] < 50)  

# img[mask] = 255
# print(img[mask].size)

# per = (mask.sum() / (img.shape[0] * img.shape[1])) * 100





# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])


# normalized = arr / arr.sum(axis= 0)
# print(normalized)



# scores = np.array([
#     [3, 1, 2],
#     [7, 5, 6]
# ])

# maxes = np.max(scores , axis=1,keepdims=True)
# print(maxes)
# print(scores - maxes)


# x = np.array([1, 4, 7, 10])

# #[1,3,7,10] , (4,)
# #[[1],[3],[7],[10]] , (4,1)
# #
# #

# print(x[:  , np.newaxis] - x)




# img = np.random.randint(
#     0 , 256,
#     (100 , 100 , 3),
#     dtype  = np.uint8
# )

# scale = np.array([1.2 , 0.8 , 1.5])

# print((img * scale).shape)




# points = np.array([
#     [1,2],
#     [4,6],
#     [7,1],
#     [3,8]
# ])


# target  = np.array([2,3])

# d =points - target

# e_dis =np.sqrt(np.sum(d**2 , axis = 1))
# print(dis)



# train = np.array([ #shape = (3,2)
#     [1,2],
#     [4,5],
#     [7,1]
# ])

# test = np.array([ # shape = (2, 2)
#     [2,3],
#     [6,2]
# ])

# x = train[np.newaxis, :]
# y = test[: , np.newaxis]

# dis = y - x
# print( dis , dis.shape)

# distances = np.sqrt(np.sum(dis**2 , axis==2))

# A = np.random.rand(5, 1, 4)
# B = np.random.rand(1, 3, 1)

# print((A + B).shape)


#advance indexing

# arr = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90,100,110,120]
# ])

# cols = np.array([2, 0, 3])

# print(arr [[0,1,2]  , cols])



# arr = np.array([
#     ["A", "B"],
#     ["C", "D"],
#     ["E", "F"],
#     ["G", "H"]
# ])

# print(arr[[-1 , 0 , -1 , 1] , :])


# arr = np.arange(1,26).reshape(5,5)

# print(arr[[0, 0,-1,-1], [0,-1 , 0 ,-1]])


# img = np.random.randint(
#     0,256,
#     (100 , 100 , 3),
#     dtype = np.uint8
# )

# rows = np.array([10, 30, 50, 70])
# cols = np.array([20, 40, 60, 80])

# print(img [rows , cols , :])



# arr = np.arange(27).reshape(3,3,3)

# print(arr[[0,1,2],[0,1,2],[0,1,2]])

# probs = np.array([
#     [0.1, 0.7, 0.2],
#     [0.8, 0.1, 0.1],
#     [0.2, 0.3, 0.5],
#     [0.05,0.9,0.05]
# ])

# labels = np.array([1, 0, 2, 1])

# print(probs[[0,1,2,3],labels])



# arr = np.arange(1,10).reshape(3,3)

# print(arr[[0,1],[1,2]])

# print(arr[np.ix_([0,1],[1,2])])





#advance indexing + sclicing

# arr = np.arange(1,31).reshape(5,6)
# print(arr)

# print(arr[0::2 ,[1,3,-1]])
# print(arr[[0,2,-1], 1::2])


# arr = np.arange(1,37).reshape(6,6)
# print(arr)
# print(arr[::2, [1,3]])


# arr = np.arange(1,26).reshape(5,5)
# print(arr)

# print(arr[::-1 , [-2 , -1]])


# img =  np.random.randint(
#     1, 256,
#     (100 , 100 , 3),
#     dtype = np.uint8
# )

# print(img[: , : , [-1,1,0]])


# img = np.random.randint(
#     0,256,
#     (100,100,3),
#     dtype=np.uint8
# )

# croped_img = img[20 : 80 , 30 : 90]
# print(croped_img[[0,10,20,30], [0,10 , 20 ,30], : ])


# arr = np.arange(1,50).reshape(7,7)
# z = arr[1: 6 , 2: 6]
# print(z)

# print(z[[0, 2 , -1], [0 , 2, -1]])



# arr = np.arange(1,17).reshape(4,4)
# result = arr[1:4, [0,2]] #  (3 ,2)
# print(result)



# scores = np.array([
#     [80, 75, 90],
#     [45, 60, 55],
#     [92, 88, 95],
#     [50, 48, 52]
# ])

# mask = scores > 70
# print(scores[mask])
# print(scores[mask].size)
# print(scores[mask].mean())


# arr = np.array([
#     [10, 25, 30],
#     [5, 40, 15],
#     [50, 20, 35]
# ])

# mask = arr < 20
# arr[mask] = 0
# arr[arr > 30] = 100

# print(arr)



# temps = np.array([
#     12, 18, 22, 28, 35,
#     40, 15, 25, 30, 8
# ])

# mask  = (temps  >= 20 ) & (temps <= 30)
# print(temps[mask])
# print(temps[mask].size)

# mask2 = (temps < 15) | (temps > 35)
# print(temps[mask2])



# marks = np.array([
#     [80, 75, 90],
#     [45, 60, 55],
#     [92, 88, 95],
#     [50, 48, 52]
# ])


# mask = (marks > 70).all(axis = 1)
# mask2 = (marks < 50).any(axis = 1)
# print(mask)
# print(mask2)
# print(marks[mask])
# print(marks[mask2])




# image = np.random.randint(
#     0, 256,
#     size=(100, 100, 3),
#     dtype=np.uint8
# )

# print(image)
# print(image[image[: , : ,0] > 200])
# image[image[: ,: ,0] > 200] = [255,0,0]
# image[(image[: ,:,1] > 150) & (image[: ,: ,2] < 50)] = [255,255,255] 



# arr = np.arange(1, 10).reshape((3,3))
# print(arr)

# scale = np.array(   [[10],
#                     [20],
#                     [30]])

# result = arr * scale
# print( result)
# print(result.shape)


# arr = np.arange(12).reshape(3,4)

# vec = np.array([1,2,3])

# result = arr + vec # no broadcasting does not work here as the shape of vector is (3,) and the arr is (3,4) the numpy tries to matches 3 with 4 which does not work so here the broadcasting doesnot work


# arr = np.ones((2,3,4))

# bias = np.array([10 , 20 ,30 , 40]) #treat it as (2,3,4)

# result = arr + bias  #resuting shape (2,3,4)
# print(result) 


# arr  = np.arange(24).reshape(2,3,4)

# print( arr)
# weights = np.array([
#     [1],
#     [10],
#     [100]
# ])


# result = arr * weights
# print( result)



# a = np.arange(6).reshape(2,3)

# b = np.array([
#     [[1]],
#     [[10]]
# ])

# print(b.shape)

# result = a + b


# a = np.ones((2,1,3))
# b = np.arange(8).reshape(2,4,1)

# result = a + b


# arr = np.arange(1 , 21).reshape(5,4)

# rows = [0,2,4]

# print( arr[rows].shape)
# result = arr[rows] + np.array([10 , 20 , 30 , 40])


# arr = np.arange(1, 21).reshape(5,4)

# rows = [1,3]

# increments = np.array([
#     [100],
#     [1000]
# ])

# print( arr[rows].shape)

# result = arr[rows] + increments

# arr = np.arange(1,26).reshape(5,5)

# rows = [0,2,4]
# cols = [1,3]
# print( arr[rows].shape)

# result = arr[rows][:, cols]
# print(result.shape)



# arr = np.arange(1,26).reshape(5,5)

# cols = [0,2,4]

# selected = arr[:, cols]

# bias = np.array([100,200,300])

# result = selected + bias



# arr = np.arange(24).reshape(2,3,4)

# batch = [0,1]

# print( arr[batch].shape)
# result = arr[batch] + np.array([100,200,300,400])



# arr = np.arange(36).reshape(6,6)

# rows = [0,2,4]

# selected = arr[rows]

# result = selected * np.array([
#     [1],
#     [10],
#     [100]
# ])


# scores = np.array([
#     [80, 75, 90],
#     [45, 60, 55],
#     [92, 88, 95],
#     [50, 48, 52]
# ])

# rows = [0 , 2]

# selected = scores[rows]

# bonus = np.array([5,10,15])

# result = selected + bonus
# mask = result > 95


np.random.seed(123)
arr = np.random.randint(1 , 8 , (7))

print(np.sort(arr))
print(np.argsort(arr))
print(np.argmax(arr))
print(np.argmin(arr))


arr = np.array([1,3,5,7,9])
print(np.searchsorted(arr , 4, side='right'))
