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


# np.random.seed(123)
# arr = np.random.randint(1 , 8 , (7))

# print(np.sort(arr))
# print(np.argsort(arr))
# print(np.argmax(arr))
# print(np.argmin(arr))


# arr = np.array([1,3,5,7,9])
# print(np.searchsorted(arr , 4 ))

# points = np.array([
#     [1, 2],
#     [4, 6],
#     [7, 1],
#     [2, 8]
# ])

# x = points[ : , np.newaxis]
# print((points - x)) (4,4,2)




# scores = np.array([
#     [80, 60, 90, 70],
#     [50, 40, 60, 30],
#     [95, 85, 75, 65]
# ])


# mask = scores > scores.mean(axis = 0)
# print(mask)



# a = np.array([3, 10, 17, 25])
# b = np.array([1, 5, 12, 18, 30])

# z = a[: , np.newaxis]
# print(np.abs(z -b))
# idx = np.abs(z-b).argmin(axis =1)
# print(b[idx])



# pixels = np.array([
#     [255, 0, 0],
#     [250, 10, 5],
#     [0, 255, 0],
#     [10, 240, 15]
# ])

# reference = np.array([
#     [255, 0, 0],    # red
#     [0, 255, 0],    # green
#     [0, 0, 255]     # blue
# ])

# z = reference[: , np.newaxis]
# print(z)
# print(z - pixels)



# sales = np.array([
#     [100, 120, 80],
#     [200, 150, 170],
#     [90, 95, 100],
#     [300, 310, 290]
# ])

# targets = np.array([110, 140, 150])

# mask = sales > targets
# print(mask)

# rows_exceeded = np.count_nonzero(mask , axis =1) 

# rows_exceeded_2 = np.count_nonzero(mask , axis=1) > 2
# print(rows_exceeded)
# print(rows_exceeded_2)

# np.random.seed(123)
# A = np.random.randint(0,100,(100,5))

# print(A)

## Broadcasting practice
# points = np.array([
#     [1, 2],
#     [4, 6],
#     [7, 1],
#     [2, 8]
# ])

# z = points[ : , np.newaxis]
# dif = np.abs(z - points)


# distance = np.sum(dif , axis= 1)
# print(distance)



# arr = np.array([3, 8, 2, 10, 5])


# z = arr[: , np.newaxis]


# diff = arr - z

# r = np.where(diff > 0 , diff , -1)

# print(r)
# r = (r < 0).all(axis = 1)
# print(r)


# points = np.array([
#     [1, 2],
#     [4, 6],
#     [7, 1],
#     [3, 8]
# ])

# z = points[   :, np.newaxis]
# dif =np.abs( z- points)

# result = np.sum(dif , axis = 1)
# print(result)


# arr = np.array([
#     [10, 15, 20],
#     [5,  7,  9],
#     [30, 40, 50]
# ])

# targets = np.array([18, 6, 35])

# dis = arr - targets[:  , None]

# print(dis)

# idx = np.argmin(abs(dis) , axis=1)
# print(idx)


# print(arr[np.arange(arr.shape[0]), idx])


# points = np.array([
#     [1, 2],
#     [4, 6],
#     [7, 1],
#     [3, 8]
# ])

# x = points[ : , None , :]
# y = points[None , : , : ]

# dis =  np.abs(x - y)

# dis = dis.sum(axis = -1)
# print(dis)


# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# scale = np.array([10, 20, 30])


# print(A * scale)


# x = np.array([1, 4, 7, 10])

# p = x[: , None]
# print(p)

# print(p - x)



# points = np.array([
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ])

# centers = np.array([
#     [0, 0],
#     [10, 10]
# ])
# points = points[: , None]
# centers = centers[None,:]
# print(points.shape)
# print(centers.shape)
# res = points - centers
# print(res.sum(axis = 1))
# print(res.shape)



# image  = np.random.randn(100 , 100 , 3)
# factors = np.array([1.2 , 0.8 , 1.5])


# image *= factors


# scores = np.array([
#     [2, 5, 3],
#     [8, 1, 4],
#     [6, 7, 2]
# ])


# row_max = np.max(scores , axis= 1)
# row_max  = row_max[: , None]
# print(row_max)
# print(scores  - row_max)


# points = np.array([
#     [1, 2],
#     [4, 6],
#     [7, 1],?.---------------------------------
#     [3, 8]
# ])

# x = points[:  , None]
# y = points[None, :]
# print(x.shape)
# print(y.shape)
# print(x)
# print()
# print(y)

# z = x - y
# z= np.sum(z,axis=-1)
# print(z.shape)
# print(z)




# arr = np.array([
#     [10, 15, 20],
#     [5,  7,  9],
#     [30, 40, 50]
# ])

# targets = np.array([18, 6, 35])
# targets = targets[: , None]
# z = np.abs(arr - targets)

# idx =  np.argmin(z, axis=1)
# print(arr[np.arange(0, arr.shape[0]) , idx])


# arr = np.array([
#     [7, 2, 9],
#     [1, 5, 4],
#     [8, 3, 6]
# ])

# x = arr[: ,None , :]
# y = arr[None, : , :]

# z = x > y
# print(z)
# print(z.sum(axis=1) + 1)

# arr = np.array([
#     [5, 2, 7],
#     [4, 1, 6],
#     [8, 3, 9],
#     [2, 0, 5]
# ])

# x = arr[: , None , :]
# z = x > arr

# res = (z.all(axis  = 2)).sum(axis = 1)
# print(res)


# vectors = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [1, 0, 1],
#     [2, 1, 0]
# ])


# x = vectors[: , None, :]
# y = vectors[None, : ,:]

# dot = (x * y).sum(axis= 2)


# norm = np.linalg.norm(vectors, axis=1)   # (n,)


# denom = norm[: , None] * norm[None , : ]

# sim = dot/denom
# print(sim)

# np.random.seed(123)
# arr = np.random.randint(0, 256 , (1000, 5))
# print(arr)

# x = arr[: , None , :]

# dif = x- arr[None , : , :]

# distance = np.sqrt(np.sum(dif**2 , axis = 2))



# np.fill_diagonal(distance , np.inf)

# idx  = np.argmin(distance)
# idx = np.unravel_index(idx , distance.shape)
# print(idx)


# arr = np.array([
#     [7, 2, 9, 4],
#     [1, 5, 4, 8],
#     [8, 3, 6, 1],
#     [2, 9, 5, 7]
# ])

# x = arr[: , None , : ]
# y  = arr[None , :, :]

# r_y = arr[: , : , None]

# z = x > y
# i = r_y > x
# col_rank = z.sum(axis = 1) + 1
# print(col_rank)
# row_rank = i.sum(axis = 2) + 1
# print(row_rank)


# arr = np.array([
#     [8, 3, 7],
#     [5, 2, 6],
#     [7, 3, 5],
#     [4, 1, 4],
#     [6, 2, 8]
# ])


# x = arr[: , None , :]
# y = arr[None , : , :]

# z = x - y

# res= (z > 0 ).all(axis = 2).sum(axis=1)
# print(res)



# np.random.seed(123)
#arr = np.random.randint(0,100,(20,10))

# print(arr)

# arr = arr.T

# x = arr[: , None , :]
# y = arr[None , : , : ]

# z = x - y

# dis = np.sum(z ** 2 , axis = 2)
# dis = dis.astype(float)

# np.fill_diagonal(dis , np.inf)
# idx = np.unravel_index(np.argmin(dis) , dis.shape)
# print(idx)


# arr = np.random.randn(100, 8)


# x = arr.mean(axis = 0 , keepdims = True)

# z = arr - x

# dot = (z.T @ z)

# norm = np.linalg.norm(z, axis=0)
# d_norm = norm[: , None] * norm[None , :]
# print(dot / d_norm)

# np.random.seed(123)
# points = np.random.randint(0,20,(5,3))

# diff = points[: , None , : ] - points[None , : , :]

# distance = np.sqrt(np.sum(diff **2 , axis = 2))
# print(distance)
# np.fill_diagonal(distance , np.inf)

# indexes = np.argmin(distance , axis = 1)
# print(indexes)



#TODO : problem no 6 is left
# np.random.seed(12345)
# arr = np.random.randint(0,20,(50,4))

# print(arr)

# z = arr[: , None , : ] < arr[None , : , :]
# print(z)



# print((z.sum(axis = 2) >= 3).sum(axis = 1))

# arr = np.random.randint(0,5,(200,6))
# print(arr)
# z = arr[: , None , : ] == arr[None , : , :]
# print(z.sum(axis = 2))



# arr = np.random.randint(0,100,(100,5))

# z = arr[: , None , :] - arr[None , : , :]
# print(z)

# distance = np.sqrt(np.sum(z ** 2, axis = 2))
# print(distance)


# d0 = distance[: , 0 ]

# res = d0[: , None] < distance
# print(res.sum(axis = 0))


# np.random.seed(123)
# arr = np.array([
# [ 7 , 2 , 4],
#  [ 4 , 3 , 3],
#  [ 5, 11, 14],
#  [10 ,11 ,10],
#  [ 9 ,16 , 4]])


# print(arr)

# z = arr[: , :, None] > arr[: , None ,:]
# print(z)

# res = (z).sum(axis = 0)
# print(res)

# np.random.seed(123456)
# points = np.random.randint(0,10,(5,2))

# print(points)

# z = points[: , None , :] - points[None ,:,:]
# z = (np.sum(z ** 2 , axis = 2))


# res =   z[: ,: ,None ] - z[: , None  , : ] 

# count = z[: ,: ,None ] < z[: , None  , : ] 
# print(count.sum(axis = 2).sum(axis = 1))

# np.random.seed(123456)
# arr = np.random.randint(0,10,(5,4))

# print(arr)
# z = arr[: , : , None] > arr[: ,None ,: ]

# print(z.all(axis= 0).sum(axis = 1))


# arr = np.random.randint(0,100,(50,6))

# z = arr[: , : , None ] > arr[: , None ,:]

# res = (z.sum(axis = 1) > 4)


# # score = res.sum(axis = 0) - ((arr[: , : , None ] < arr[: , None ,:]).sum(axis = 1)>4).sum(axis = 0)
# # print(score)
# np.random.seed(1234)
# arr = np.random.randint(0, 10, (5, 4))

# c_mean = arr.mean(axis = 0)

# print(c_mean)
# print(arr)
# centered = arr- c_mean


# arr = np.random.randint(1, 100, (30, 5))

# std_mat = (arr - arr.mean(axis =0) ) / np.std(arr , axis = 0)
# print(std_mat)



# arr = np.random.randint(0, 100, (15, 4))

# norm = (arr - np.min(arr , axis = 0)) / (np.max(arr , axis = 0) - np.min(arr , axis = 0))
# print(norm)


# arr = np.random.randint(0, 100, (10, 5))

# print(arr)
# print(np.argmax(arr , axis = 1))

# np.random.seed(1234)
# arr = np.random.randint(0, 20, (6, 4))
# print(arr)
# mean = arr.mean(axis = 0)
# print(mean[: , None] - mean)



# arr = np.random.randint(1, 10, (8, 3))


# dot_product = arr[: , : , None] * arr[: , None ,:]
# print(dot_product)

# norm  = np.linalg.norm(arr , axis = 0)

# d_norm = norm[: , None] * norm[None , :]
# print(dot_product / d_norm)


# arr = np.array([
#     [7, 2, 9],
#     [1, 5, 4],
#     [8, 3, 6]
# ])

# z = arr[: , None, :] >  arr[None, : , :]

# print(z.sum(axis = 1) + 1)


# arr = np.random.randint(0, 10,(5,6))
# print(arr)
# z = arr[: , : , None ] - arr[: ,None ,:]
# #(20 , 6, 1)  (20 , 1, 6) == (20 , 6 , 6)
# # z[2,1,3] = arr[2,1] - arr[2,3]
# #z[i,j,k] = arr[i,j] - arr[i,k]

# dis = np.sqrt(np.sum(z**2 , axis = 0))
# np.fill_diagonal(dis , np.inf)
# print(np.argmin(dis , axis = 1))



# arr = np.random.randint(0,100,(50,5))


# z = arr[: , : , None] > arr[: ,None , :]

# d = z.sum(axis = 0)
# print(d > arr.shape[0] // 2)


# arr = np.random.randn(100,8)


# z = arr[: , : , None]  * arr[: , None , :]

# dot_product = z.sum(axis = 0)

# norm = np.linalg.norm(arr , axis=0)

# d_norm = norm[: , None] * norm[None , :]


# corelation  =  dot_product / d_norm
# np.fill_diagonal(corelation , -np.inf)
# print(np.argmax(corelation , axis = 1))




# arr = np.random.randint(0,10,(30,7))

# z = arr[: , : , None] == arr[ : , None ,:]

# print(z.sum(axis = 0))


##pairwise column correlation matrix
# arr = np.random.randn(200, 8)

# arr= arr - arr.mean(axis =0)

# z = arr[: , : , None] * arr[: , None , :]

# dot_product =  np.sum(z , axis = 0)

# norm = np.linalg.norm(arr , axis = 0)

# d_norm = norm[: , None] * norm[None , :]

# corelation = dot_product / d_norm

# print(corelation)


#Nearest Column
# arr = np.random.randn(100, 12)

# z = arr[: , : , None] - arr[: , None , :]

# dist = np.sqrt(np.sum(z**2 , axis = 0))

# print(dist)
# np.fill_diagonal(dist , np.inf)

# nearest = np.argmin(dist , axis = 1)
# print(nearest)



#Column Dominance Tournament


# arr = np.random.randint(0,100,(50,7))


# z = arr[: , : , None] > arr[: , None ,:]

# d = z.sum(axis = 0)

# wins = d >( arr.shape[0]//2)
# print(wins)

# score = wins.sum(axis = 1) - wins.sum(axis = 0)


# print(score)



# points = np.random.randint(0,100,(300,4))


# z = points[: , None , :] - points[None , : , :]

# max_dif = np.abs(z.max(axis = 2))
# print(max_dif.shape)

#Problem 5 — Similarity by Sign Pattern

# arr = np.random.randn(500,10)


# arr[arr > 0]  = 1
# arr[arr < 0] = 0


# z = arr[: , None ,:] == arr[None  ,: , :]
# print(arr)
# print(z.sum(axis = 2))



# arr = np.random.randint(0,100,(100,8))

# z = arr[: , None, :] > arr[None ,:  , :]


# beats = z.all(axis = 2)
# print(beats)


# dominance_score = beats.sum(axis = 1) - beats.sum(axis = 0)
# print(dominance_score)


# np.random.seed(12345)
# arr = np.random.randint(0 , 10,(5,3))


# print(arr)

# sum = np.sum(arr  , axis = 1)

# x = arr[: , None ,:] - arr[None ,: ,:]

# distance = np.sqrt(np.sum(x**2 , axis = 2))

# z = sum[: , None ] < sum[None , : ]





# stronger_neighbour  = np.where(z , distance , np.inf)
# print(z)
# print(distance)
# nearest = np.argmin(stronger_neighbour , axis = 1)
# print(nearest)


# arr = np.random.randint(0,2,(300,12))


# z = arr[: , None , :] == arr[None , :,:]


# agreements = np.sum(z , axis = 2)

# print(agreements)

# connected = agreements >= 10

# print(connected)

# network_score = np.sum(connected , axis = 1)
# print(network_score)



# arr = np.random.randint(0,100,(150,8))


# z = arr[: ,None ,:] > arr[None ,: ,:]


# beats = z.sum(axis = 2) >= 5
# print(beats)
# print(beats.shape)
# elite_mask = beats.sum(axis = 1) >= (arr.shape[0]*0.6)
# print(elite_mask)

# elite_rows = arr[elite_mask]


# elite_similarity = (arr[: ,None ,:] == elite_rows[None ,: ,:]).sum(axis = 2).mean(axis = 1)
# print(elite_similarity)



# points = np.random.randn(500,3)


# z = points[: , None ,:] - points[None , : ,:]

# dis = np.sqrt(np.sum(z**2 , axis = 2))

# neighbor = (dis <= 0.5)
# neighbor_count = neighbor.sum(axis = 1)
# print(neighbor_count)

# avg_neighbour_distance = np.where(neighbor , dis, 0).sum(axis  =1)/neighbor_count
# print(avg_neighbour_distance)



# arr = np.random.randint(0,100,(400,10))

# groupA = arr[: 200]
# groupB = arr[200:]


# prototypeA = groupA.mean(axis = 0)

# prototypeB = groupB.mean(axis = 0)

# distance_to_proA =np.sqrt(np.sum(( arr - prototypeA)**2 , axis=1))
# distance_to_proB = np.sqrt(np.sum((arr - prototypeB)**2 , axis = 1))


# prediction = np.where(distance_to_proA < distance_to_proB , 0 , 1)
# # print(prediction)






# arr = np.random.randint(0,100,(100,6))


# z = np.abs(arr[: , None , :] - arr[None, : , :])
# dis = z <= 5

# Similarity = dis.sum(axis = 2)
# print(Similarity)

# connected = Similarity >= 5

# influence = arr.sum(axis = 1)
# print(connected)
# print(influence)


# propagated = np.sum(connected * influence , axis = 1)
# print(propagated)




# arr = np.random.randint(0,100,(120,7))


# z = arr[: , None ,:] > arr[None ,: ,:]

# beats = np.sum(z , axis = 2) >= 4

# direct_score = np.sum(beats,axis= 1) - np.sum(beats , axis = 0)
# print(direct_score)


# opponent_strength = beats @ direct_score

# final_score = direct_score + opponent_strength
# print(final_score)



# arr = np.random.randint(0,100,(300,8))


# z = arr[: , None ,:] > arr[None , : ,:]

# dominance_count  = np.sum(z , axis = 2)


# edge = dominance_count >= 6

# power = np.sum(arr , axis = 1)

# inherited_power =  edge @ power

# rank = power + inherited_power
# print(rank)


# arr = np.random.randint(0,100,(250,6))

# z = arr[: , None , :  ] - arr[None , : ,:]


# similarity = (np.abs(z) <=10).sum(axis = 2)
# rivals = similarity >= 5
# rival_count  = rivals.sum(axis = 1)
# strength = np.sum(arr, axis =1)

# rivals_strength = (rivals @ strength)  / rival_count


# store = strength - rivals_strength
# print(store)


#Problem 2 — Influence of Influencers

# arr = np.random.randint(0,10,(180  , 7))

# z = arr[: , None ,:] > arr[None , : ,:]


# beats = np.sum(z , axis = 2) >= 5



# wins = np.sum(beats , axis = 1)


# influencers = wins > 100


# distance = (arr[: , None ,:] - arr[influencers])
# distance = np.sqrt(np.sum(distance **2 , axis = 2)).mean(axis = 1)



#Problem 3 — Neighborhood Consensus

# arr = np.random.randint(0,50,(300,8))

# z = arr[: , None ,: ] - arr[None ,: ,:]

# distance = np.sqrt(np.sum(z**2 , axis = 2))


# np.fill_diagonal(distance , np.inf)

# neighbor = np.argmin(distance  , axis = 1)
# print(neighbor.shape)



# arr = np.random.randint(0,100,(150,7))

# z = arr[: , None , :] >  arr[None ,: ,:]

# dominates = np.sum(z , axis = 2) >= 5
# print(dominates)


# direct_power = np.sum(dominates , axis = 1)

# indirect_power = dominates  @ direct_power
# print(indirect_power)
# grand_power = direct_power + indirect_power




# points = np.random.randn(400,4)

# z = points[: , None ,:] - points[None ,: ,:]

# distance = np.sqrt(np.sum(z **2 , axis = 2))

# connected = distance <= 1

# degree = np.sum(connected , axis = 1)

# thres_hold = np.percentile(degree , 90)

# core_points = degree >= thres_hold

# print(distance[: , core_points].shape)
# nearest_core_distance =  np.min(distance[: , core_points] , axis = 1)
# print(nearest_core_distance.shape)




# ratings = np.random.randint(1,6,(500,20))

# z  =ratings[:  , None ,:] - ratings[None , : ,:]

# agreement = np.sum(z , axis = 2) <= 1

# friends = agreement >= 15


# friend_profile = friends @ ratings
# print(friend_profile.shape)

# recommendation_score = friend_profile - ratings


# print(recommendation_score.shape)
# recommended_item = np.max(recommendation_score , axis = 1)
# print(recommended_item.shape)



# arr = np.random.randint(0,100,(200,6))


# z = arr[: , None , :] - arr[None ,: ,:]
# #(200,200,6)
# distance = np.sqrt(np.sum(z**2 , axis = 2))
# #(200 x 200) distance between all rows

# np.fill_diagonal(distance , np.inf)

# neighbour = np.argsort(distance , axis = 1)

# nearest_neighbour = neighbour[: , : 5]
# #(200 x 5)  five nearest neighbour
# print(nearest_neighbour)

# power = np.sum(arr , axis = 1)
# #(200)

# neighbour_power = power[nearest_neighbour].mean(axis = 1) 


# influence_score = power - neighbour_power



# arr = np.random.randint(0,100,(250,7))


# z = arr[: , None , :] - arr[None ,: ,:]
# #(250 , 250 , 7)
# similar = (np.abs(z) <= 10).sum(axis = 2)
# #(250 x 250)


# friends = similar >= 6
# friends_count = np.sum(friends , axis = 1)
# #(250 x 250)
 

# strength = np.sum(arr , axis= 1)
# #(250 x 250)

# friend_strength = (friends @ strength) / friends_count
# #(250,)
# print(friend_strength.shape)




# arr = np.random.randint(0,100,(180,8))


# z = arr[: , None ,: ] > arr[None , :,:]
# #(180 x 180 x8)
# wins = np.sum(z , axis = 2)
# #(180 x 180)


# dominates = wins >= 6
# #(180 x 180)

# power = np.sum(dominates , axis = 1)
# #(180 ,)


# inherited_power =  dominates @ power
# #(180,)

# rank = power + inherited_power




# arr = np.array([
#     [9, 8, 7, 6],   # A (0)
#     [8, 7, 6, 5],   # B (1)
#     [7, 6, 5, 4],   # C (2)
#     [6, 5, 4, 3],   # D (3)
#     [5, 4, 3, 2],   # E (4)
#     [1, 1, 1, 1]    # F (5)
# ])

# z = arr[: , None ,: ] - arr[None , : , :]
# #(6,6,4)
# distance = np.sum(np.abs(z) , axis = 2)
# #(6,6)

# connected = distance <= 8
# #(5,5) --> adjancy matrix shows a direct connection between i and j
# np.fill_diagonal(connected , False)

# connection_count = np.sum(connected , axis = 1)
# #(5,5) connection count 
# degree = np.sum(connected , axis  =1)
# #(5,) no of direct connection of i with other row


# friend_degree =( connected @ degree) / connection_count
# #(5,5) x (5, ) => #(5,) / (5,) => (5,) Average of degree of al the conection of of i 

# two_hops = connected @ connected
# #(5,5) x (5,5) =>(5, 5) no of paths of length 2

# two_hops[connected] = False
# np.fill_diagonal(two_hops , False)
# print(two_hops)
# tow_hops_count = np.sum(two_hops , axis= 1)
# print(two_hops)


# recommendation_score = (two_hops @ degree) / tow_hops_count
# #(5,5) x#(5 ,) => (5,) / (5,) => (5,)
# print(recommendation_score)



# A = np.array([
#     [1,1,1,0],
#     [1,1,0,1],
#     [1,0,1,1],
#     [0,1,1,1]
# ])

# print(A @ A)


# arr = np.random.randint(0, 100, (180, 8))
# #(180 , 8)
# z = arr[: , None , :] - arr[None ,: ,:]
# #(180 , 180 , 8)
# z = np.abs(z) <= 10

# trust = np.sum(z , axis = 2) >= 6
# print(trust)
# #(180 , 180)
# np.fill_diagonal(trust , False)
# trust_count = np.sum(trust , axis = 1)



# influence  = np.sum(arr , axis = 1)

# trusted_influence = (trust @ influence) / trust_count
# #(180 ) x (180 , 180) = (180 , ) / (180 ,) = (180 , )



# mutual_trust = trust.astype(np.int16) @ trust.T.astype(np.int16)
# np.fill_diagonal(mutual_trust , 0)
# mutual_trust[trust] = 0
# mutual_trust = mutual_trust >=2

# mutual_trust_count = np.sum(mutual_trust , axis = 1)

# #(180 , 180)
# print(mutual_trust)




# recomendation_score = (mutual_trust @ influence) / mutual_trust_count


# np.seterr(divide='ignore', invalid='ignore')
# purchases = np.random.randint(0, 50, (250, 12))
# #(250 , 12)
# z = purchases[: , None , :] - purchases[None ,: ,:]
# #(250 , 250 , 12)
# similar = np.abs(z) <= 3

# compatible_customers = np.sum(similar , axis = 2) >= 9
# #(250 , 250 ) =>  a  single cell represents if a customer[i] is  compatible with customer[j]

# np.fill_diagonal(compatible_customers , False)
# #removing compatibility with itself
# compatible_customers_count = np.sum(compatible_customers ,axis = 1)


# customer_value = np.sum(purchases , axis =1)
# #(250 , ) customer value as sum of products they purchased 


# community_value = np.divide((compatible_cutomers @ customer_value) , compatible_customers_count )
# # (250 , 250) x(250  ,) => (250 ,)


# hidden_communities = (compatible_customers.astype(np.int16) @ compatible_customers.T.astype(np.int16))
# #(250 , 250) x (250 , 250) => (250 , 250) common customers
# np.fill_diagonal(hidden_communities , 0)
# #(removing relationship with itself)
# hidden_communities[compatible_customers] = 0
# # removing direct compatile customers
# hidden_communities = hidden_communities >= 4
# #thresholding

# hidden_com_count = np.sum(hidden_communities , axis = 1)
# #(250)
# premium_score =  (hidden_communities @ community_value) / hidden_com_count
# #(250)

# community_leader = premium_score > community_value
# print(community_leader)

# leader_exposure = (hidden_communities @ community_leader.astype(np.int16))
# print(leader_exposure)


#Problem 2 — Student ↔ Course Ecosystem


# scores = np.random.randint(0 , 101, (300 , 40))
# # each cell represensts the student's score in that course


# average_course_score = np.mean(scores , axis = 0) 
# #(40 ,)

# course_difficulty = average_course_score
# # each cell represents the average of scores achieved by students in particular courses
# student_strength = np.mean(scores, axis = 1)
# # each cell represents a student's academic strength 
# #(300)
# print(student_strength)

# z = scores[: , None ,: ] - scores[None , : ,:]

# z = np.abs(z) <= 8

# student_similarity = np.sum(z , axis = 2) >= 30
# #(300 , 300) each cell represents  whether a student i is similar with student j 


# np.fill_diagonal(student_similarity , False)

# similar_student_count = np.sum(student_similarity , axis = 1)

# study_group_strength = (student_similarity @ student_strength) / similar_student_count
# #(300 , 300) , #(300) => (300,)
# #each cell represents the average student strength of all the similar student


# y = scores[: , : , None] - scores[: , None, :]

# z = np.abs(y) <= 5

# related_course = np.sum(z , axis = 0) >= 180
# #(40 , 40) every cell represents if course i is similar to course j
# np.fill_diagonal(related_course , False)

# related_course_count = np.sum(related_course , axis = 1) #no of related course with course i

# knowledge_flow = np.divide((related_course @ course_difficulty) , related_course_count )
# #(40, )

# x = scores >= 80
# x_count = np.sum(x , axis = 1)

# learning_environment = (x @ knowledge_flow) / x_count
# #(300 , 40) x(40) =>(300, )



# customer_product = np.random.randint(0, 6, (400, 80))
# #every cell represents how many times a customer purchased a particular product

# store_product = np.random.randint(0, 2, (60, 80))
# # each cell can be 1 if the store stock the product or 0 otherwise


# customer_value = np.sum(customer_product , axis = 1)
# #(400)

# product_popularity = np.sum(customer_product , axis = 0)
# #(80)

# stock_count = np.sum(store_product , axis = 1)

# store_strength = (store_product @ product_popularity) /stock_count



# z = customer_product.astype(np.bool) @ customer_product.T.astype(np.bool).astype(int)
# print(z)
# similar_customer = z  >= 25
# np.fill_diagonal(similar_customer , False)



# x = similar_customer @ similar_customer.T.astype(int)

# print(x)
# hidden_customer_group = x   >= 10
# hidden_customer_group[similar_customer] = False
# np.fill_diagonal(hidden_customer_group , False)
# print(hidden_customer_group)


# store = (customer_product.astype(np.bool) @ store_product.T) 
# print(store.shape)



# coverage = store / customer_product.astype(np.bool).sum(axis = 1 , keepdims = True)
# print(coverage)
# qualified_store = coverage >= 0.8

# qualified_count = qualified_store.sum(axis=1)

# favorite_store_score = np.divide(
#     qualified_store @ store_strength,
#     qualified_count,
#     where=qualified_count != 0
# )





# ratings = np.random.randint(0, 6, (500, 60))

# watched_movies = ratings.astype(np.bool)
# # stores if a user has watched a movie or not


# common_movies_count = watched_movies.astype(int) @ watched_movies.T
# #(500 , 500) one single cell represents how many movies both user i and j has watched
# np.fill_diagonal(common_movies_count  ,0 )

# similar_users =  np.argsort(common_movies_count , axis= 1)
# best_friend = np.argsort(common_movies_count , axis= 1)[ : , -1 : -11 : -1]
# #  (500 , 10) each row contains the 10 most similar user with the user i



# recommendation_strength = (watched_movies[best_friend]).sum(axis =1 )

# recommendation_strength_thres = recommendation_strength > 6
# recommended_movies = recommended_movies = (~watched_movies) & (recommendation_strength > 6)
# print(recommended_movies)



# 350 researchers
# 120 papers
# 25 research topics



# researcher_paper = np.random.randint(0, 2, (350, 120))
# #(researcher , papers ) whether researcher authored the topic or not
# paper_topic = np.random.randint(0, 2, (120, 25))
# #(paper , topics) whether the paper belongs to this topic or not


# research_activity = np.sum(researcher_paper , axis=1) 
# # no of papers a researcher has contributed to (350  ,)

# researcher_topic = (researcher_paper @ paper_topic)
# topic_popularity = (researcher_topic   > 0).sum(axis = 0)

# expertise = ((researcher_topic  > 0) @ (topic_popularity)) / (researcher_topic > 0).sum(axis= 1)


# collaborators = (researcher_paper @ researcher_paper.T) >= 4
# np.fill_diagonal(collaborators , False)

# expertise_collaborators = np.where(collaborators , expertise , -np.inf)
# expertise_collaborators_count = ((expertise_collaborators > 0).sum(axis = 1) > 5)

# top8= expertise_collaborators.argsort(axis = 1)[: , -1:-9:-1]

# top8_expertise = expertise[top8]

# influence_score = top8_expertise.mean(axis = 1)
# recommended_topic = (~(researcher_topic > 0 )) & ((researcher_topic[top8].sum(axis = 1) > 0) > 5)

# employee_project = np.random.randint(0, 2, (320, 90))
# project_skill = np.random.randint(0, 2, (90, 35))

# employee_skill = employee_project @ project_skill

# employee_skill_graph = employee_skill > 0

# expertise = (employee_skill > 0).sum(axis = 1)

# common_skill =  employee_skill_graph.astype(int) @ employee_skill_graph.astype(int).T
# partner = common_skill >= 20
# np.fill_diagonal(partner  , False)
# no_of_partner = (partner).sum(axis = 1)

# partner_expertise = (partner @ expertise) / no_of_partner


# top5 = np.where(partner , expertise , -np.inf).argsort(axis = 1)[: , -1 : -6:-1]

# recommend_skill = (~employee_skill_graph) & (employee_skill_graph[top5].sum(axis = 1) >= 3 )


# researcher_paper = np.random.randint(0, 2, (450, 180))
# paper_keyword = np.random.randint(0, 2, (180, 60))
# keyword_field = np.random.randint(0, 2, (60, 12))

# researcher_keyword = researcher_paper @ paper_keyword

# researcher_field =researcher_keyword  @ keyword_field
# print(researcher_field)

# field_graph = researcher_field >= 5
# common =  field_graph.astype(int) @ field_graph.astype(int).T

# partners = (common >= 8)
# np.fill_diagonals(partners , False)

# partner_count = partners.sum(axis  = 1)
# field_strength = field_graph.sum(axis = 1)
# partner_field_strength = (partners @ field_strength ) / partner_count

# top6 = np.where(partners , field_strength , -np.inf).argsort(axis = 1)[: , -1:-7:-1]

# recomment_research_field = (~field_graph) & (field_graph[top6].sum(axis = 1) >= 4)




# researcher_paper = np.random.randint(0, 2, (500, 220))
# paper_topic = np.random.randint(0, 2, (220, 45))
# conference_session = np.random.randint(0, 2, (30, 45))

# researcher_topic = researcher_paper @ paper_topic

# researcher_experience = researcher_topic >= 10
# # there are 220 paper in total and if in atlest 45 of theem if a researcher has talked about a certain topic then he must be wel knowing in that topic



# common_experience = (researcher_experience.astype(int) @ researcher_experience.T) 
# compatible_researcher = common_experience >= 15

# np.fill_diagonal(compatible_researcher , False)

# s = np.sum(researcher_experience , axis = 1)
# knowledge_gain = s - common_experience
# collaborators = np.where(compatible_researcher  , knowledge_gain , -np.inf)

# top5 = collaborators.argsort(axis = 1)[: , -1:-6:-1]

# c = researcher_experience @ conference_session.T



# exp = c[top5].sum(axis  = 1)
# print(c.shape)
# recommend_conference = (c < 7 ) & (exp >= 80)





# student_course = np.random.randint(0, 2, (550, 160))

# course_skill = np.random.randint(0, 2, (160, 50))

# mentor_skill = np.random.randint(0, 2, (220, 50))

# company_requirement = np.random.randint(0, 2, (70, 50))



# student_skill_rel = student_course @ course_skill
# #(550 , 50) no_of courses student i takes that teaches him skill j
# student_skill_pf = student_skill_rel > 0 
# #(550 , 50) whether student i knows skill j

# students_mastery = np.sum(student_skill_pf , axis = 1)
# #(550 , ) no of distinct skill the student knows

# common_skill = student_skill_pf @ mentor_skill.T
# #(550 , 220 ) no of common skill student i and mentor j shares

# compatible_mentor = common_skill >= 20
# #(550 , 220) whether a mentor is compatible with the student or not



# mentor_mastery = np.sum(mentor_skill , axis = 1)

# knowledge_gain = (mentor_mastery - common_skill)





# z = np.where(compatible_mentor,knowledge_gain,-np.inf ).argsort(axis  = 1)

# top5 = z[: , -1 : -6 : -1]


# s = mentor_skill[top5].sum(axis = 1) @ company_requirement.T

# s_c = student_skill_pd @ company_requirement

# recommended_company = (s_c  < 10) & (s >= 20)  




# user_movie = np.random.randint(0, 2, (8, 12))
# # 8 -> users
# # 12 -> movies 
# # did user i watched movie j 

# movie_genre = np.random.randint(0, 2, (12, 5))
# #12 -> movies
# #5-> genre
# # does movie j belongs to genre k


# genre_pf = user_movie @ movie_genre
# # (user , movie)
# #    @
# # (movie , genre)
# #(8,5)

# #=== (user , genre) ==> how many movies has user i watcher in genre k 


# print(user_movie)
# print()
# print(movie_genre)
# print()
# print(genre_pf)



# common_movie_watches =( genre_pf > 0 ) @ (genre_pf.T >0)

# # how many movies has user i and j watched that belongs to the same genre
# print(common_movie_watches)

# friends = common_movie_watches >= 3
# np.fill_diagonal(friends , False)




# knowledge_gain = np.sum(genre_pf, axis = 1) - common_movie_watches



# top3 = np.where(friends , knowledge_gain , -np.inf).argsort(axis = 1)[: , -1:-4:-1]
# print(top3.shape)


# ## question no 1.
# ## the shape of the top 3 mat is (8,3)
# #in which 8 -> users 
# # and 3 col are form knowledge gain which is  total_no of movies from genre watched - common_movies between user i and j

# #basically how many genre's knowledge can user i get from j 

# # top3[4 , : ] means how knowledge can user 4 gain from user its top matching user(friends)

# # question no 2

# #if top3[2] == [5,1,7]

# # it means that user 2 has not known about 5 genre that user its top friend[1] knows and 1 genre that it top friend[2] knows and 7 genre that ts top_friend [3] knows but wait there are only 5 genre so how can the value be 7??


# # question no 3


# #genre_profile[top3]
# ## it means (user x top_friends x genre)
# ## so for every user extract the genre_pf of its top3 friends
# # where genre_pf = how many movies has the user has watched in a specific genre

# # so it means for every user ectract how many movies has its each top friends has watched in each genre



# ##question no 4
#  #(8,5) (8, 3)==> (8, 3, 5)
#  #where 8_> users 3_> top 3 friedn idx , 5_> genre_pf of the top 3 friend



# ##question not 5

# #genre_profile[top3].sum(axis=1)  (8 , 3, 5)=> over friends it gives ==> (8,5)

# # one cell represents the sum of movies watched by  the each top friend of user i in every genre 





# researcher_topic = np.random.randint(0, 2, (6, 8))
# #6-> researcher
# #8-> topic
# #one cell means it researcher i had knwledge about topic j
# topic_field = np.random.randint(0, 2, (8, 4))
# #8-> topic
# #4-> field of topic
# # one cell means if topic j belongs to field k


# field_profile = researcher_topic @ topic_field
# #(researcer , topic) (6, 8)
# #  @
# #(topic , field) (8 , 4)
# # === (researcher , field) (6 , 4)
# # one cell means how many topic does researcher know that belongs to field k 


# field_strength = (field_profile > 0).sum(axis = 1)
# #(6,4) + on axis 1 == (6 , )
# # where each cell represents no of distinct research fields reacher i works in 


# common_field = (field_profile > 0 ) @ (field_profile > 0).T
# #(6, 6) no of common filed between two researcher


# collaborators = common_field >= 2
# #(6,6) whether two researcher has atleast two fields in common


# knowledge_gain = field_strength  - common_field
# #(6, ) - (6,6) = (6,6) where one single cell represents about how many field's knowledge can tow a researcher gain form another



# top2 = np.where(collaborators , knowledge_gain , -np.inf).argsort(axis = 1)[: , -1:-3:-1]
# #(6, 2)


## question 1
## if top2[3] = [4,1]
## it means that for researcher 3 its top 3 collaborators are researcher 4 and researcher 1

## question 2

#field_profile[top2]
# it means for every user extract the field_profile of its top2 colaborators


##question 3
##  the shape prediction happes this way there are 6 researcher , for every researcher we need the filed_profile of its top 2 collaborators , and there are  8 col in field_profile which means how may does does researcer has worked on that belons to this field

#so the shape is (6, 2, 8)

#question 4
# combined_fields = field_profile[top2].sum(axis=1)
#field_profile[top2] = (6,2,8) summing over axis one gives (6,2)
# which represents for researcher i  sum of no of topic each top colaborators has worked on in every field , basicially if combined_fields[5,2] == 7 it means that for researcher 5 its top2 collaborators has worked on total 7 topic belonging to specific field basically fun of field_profile of the top2 rsearcher 


## quesiton 5

# okay so instead of sum if we computed max in axis 1 we get the collaborator for a researcher how many highest no of worked on topic in fields 


# listener_song = np.random.randint(0, 2, (5, 9))
# #5-> listeners
# #9-> songs
# # each cell represents whether listener i has listened to song j

# song_genre = np.random.randint(0, 2, (9, 4))
# #9 -> songs
# #4-> genre of the songs
# # each cell represents whether song j belongs to genre k 


# listeners_genre_pf = listener_song @ song_genre
# ## (listeners , songs) @ (songs @ genre) = (listeners , genre) = (5, 4)
# # each cell represents how many songs has listener listened to that belongs to  a specific genre


# genre_mastery =( listeners_genre_pf > 0 ).sum(axis = 1)
# # no of distinct genre each listener listens to 

# shared_genre = (listeners_genre_pf > 0 ) @ (listeners_genre_pf > 0 ).T
# # no of common genre between two listeners = (5, 5)

# similar = shared_genre >= 3


# music_gain = genre_mastery - shared_genre
# #(5 , ) - (5,5) = (5,5)
# #each cell represents how much more music knowledge can listener i gain from listenre j 



# top2 = np.where(shared_genre , music_gain , -np.inf).argsort(axis = 1)[: , -1:-3:-1]
# #(5,2) for every listeer thieir top 2 similar listeners



# #question 1 
# #if top2[1] == [4,0]
# # it means for listener 1 its top two listener buddies are listener no 4 and listeer 0

# #question 2
# # genre+profile[top2] means genre_profile of the top2 listener for any listener
# # or it extracts the no of music listened by the top 2 listeners in given genres for a listener i


# #question 3 (5, 2, 4)
# # for 5 listener their top 2 listenerr budies with their genre_profile


# #question 4 buddy_genres = genre_profile[top2].sum(aixs = 1) == 1
# # if buddy_genres[2,3] == 11 then it means that for listener 2 its top 2 buddies has listener 11 songs in total belonging to certain genre
# # it means the sum of the genre_profile of the top2 listerner_buddies of listener 2


# #question 5
# #buddy_genre = genre_profile[top2].mean(axis = 1) it gives the average of total songs listener by the listener_buddies of listeners 
# # it provides the average of songs listener by the top2 listeners  and not sum


# #question 6
# #listener_song[top2]
# #this gives what songs have the top2 buddies of the lister i listened to  so they will get a something like [0,1,1,0] for both top1 and top2 which shows if they has listened to that particular song


# # yes it would makes sense , because after retreving the songs we can retrieve the genre of the songs lister has not listenerd to and recommend that




# student_course = np.random.randint(0, 2, (4, 6))

# course_skill = np.random.randint(0, 2, (6, 5))

# skill_job = np.random.randint(0, 2, (5, 3))


# student_skill = student_course @ course_skill
# ##(student , course) @ ( course , skill) => (student , skill) one cell tells how many course does student i took that teaches him skill j
# #(4,5)

# student_job =( (student_skill > 0) @ skill_job) 
# #(student , skill) @ (skill , job) => (student , job) one cell represents 
# #(4,3) one cell represents how many skill does student i knows that job k requires 


# common_job = (student_job > 0)  @ (student_job > 0).T
# #(4,4) how mant jobs does both student shares


# partners = (common_job) >= 2

# knowledge_gain = np.sum(student_job > 0 , axis = 1) - common_job
# #(4,4)




# top2 = np.where(partners , knowledge_gain , -np.inf).argsort(axis = 1)[: , -1:-3:-1]




# #question 1
# ## what information is stored in top2?
# ##the top2 contains the index of the the top2 partners of a student 
# ##
# ##

# #Question 2
# #student_skill[top2]
# # (4,5)[4,2] = [4,2,5]
# # this willl extract the no of course that the top2 partners have taken that teaches then thoase particular skill .


# #question 3

# #partner_skill = student_skill[top2].sum(axis=1)
# #combines number of courses that the top2 partners have taken in total for the two particular skill

# #quesiton 4
# #partner_job = partner_skill @ skill_job
# #wel partner_job is a combined no of courses two student has taken so combining that with if a job requires a skil pr not , i dont think it gives any meaning full ans 

# #question 5
# #partner_job[1] = [17, 9 , 21] those number can mean something 


# #question 6
# #student_job[top2]
# #student job is the number of skill that student knows that a job requires so its top2 would extract for every student extract the no of skill their top2 partner knows that qualifies a job

# #student_job[top2].sum(axis=1)
# #the no  of skill of their partner that qualifies job has lost



# doctor_patient = np.random.randint(0, 2, (5, 8))

# patient_disease = np.random.randint(0, 2, (8, 6))

# disease_treatment = np.random.randint(0, 2, (6, 4))


# doctor_disease = doctor_patient @ patient_disease

# #how many patient has doctor trated that had disease k
# # it also tells if doctor i can treat disease k

# doctor_treatment = (doctor_disease > 0) @ disease_treatment
# #one cell represents how many treatment does doctor i knows that treats disease j 


# shared_treatment = (doctor_treatment > 0) @ (doctor_treatment > 0).T 

# collaborators = shared_treatment >= 3

# knowledge_gain = np.sum((doctor_treatment > 0) , axis = 1) - shared_treatment


# top2 = np.where(collaborators , knowledge_gain , -np.inf)[: , -1:-3:-1]




# #questions 
# #1
# #top2[4] = [2,0] this means for doctor 4 his top collaborators  are doctors 2 and doctor 0

# #2
# #doctor_disease[top2]
# #for every doctor it extracts the doctor_disease vector of its top2 collaborator

# #3
# # if partner_disease[1,5] = 9 
# # for a doctor whose partner are 1,5 9  is sum of  the number of patient treated by the partner who were suffereing from a specific disease

# #for example if the data were to be
# #A   tumor cance 
# #     8      4    

# # b  tumor   cancer
# #     2        1


# # then partner_diesear will result tumor = 10 and cancer = 5



# # so it is the du mof the common disease treated by both partner doctor




# #5

# #strong_treatment = partner_treatment >= 8
# # it gives us the matrix showing if the partner doctor has a strrength of atlest  of treating a disease

# #similar_team = strong_treatment @ strong_treatment.T
# #it gives us how much similar are the treatment strength between partner doctors 
# # 
# # 6
# # 
# # top_team
# #  partner_treatment[top_team] it will give us the top two team of two member how mas the highest score for treating diease



# researcher_paper = np.random.randint(0, 2, (500, 200))

# paper_topic = np.random.randint(0, 2, (200, 40))

# conference_focus = np.random.randint(0, 2, (25, 40))


# researcher_topic = researcher_paper @ paper_topic


# researcher_conference = (researcher_topic > 0) @ conference_focus.T


# common_topic = (researcher_topic > 0 ) @ (researcher_topic > 0).T

# collaborators = common_topic >= 5

# knowledge_gain = np.sum((researcher_topic > 0) , axis = 1) - common_topic


# top3 = np.where(collaborators , knowledge_gain , -np.inf).argsort(axis = 1)[: , -1:-4:-1]


# top3_collaborators = researcher_conference[top3]

# recommended_conference = (~(researcher_conference > 0))  & (top3_collaborators.sum(axis = 1) >= 10)
# print(recommended_conference)



# customer_account = np.random.randint(0, 2, (600, 900))

# account_merchant = np.random.randint(0, 2, (900, 250))

# merchant_category = np.random.randint(0, 2, (250, 18))


# customer_merchant = customer_account @ account_merchant


# shared_merchant = (customer_merchant >  0 ) @ (customer_merchant > 0).T



# customer_merchant_category = (customer_merchant > 0) @ merchant_category

# common_merchant_category = (customer_merchant_category > 0) @ (customer_merchant_category> 0).T


# sus_cus = (shared_merchant >= 10)

# sus_cus_2 = (common_merchant_category >= 10)

# risk_rate = shared_merchant + common_merchant_category

# print(sus_cus.shape)
# print(sus_cus_2.shape)


# suspiscious_customers = np.where(sus_cus & sus_cus_2 , True  , False)


# top3 = np.where(suspiscious_customers , risk_rate , -np.inf).argsort(axis = 1)[: , -1: -4 : -1]



# risk_profile = customer_merchant_category[top3].sum(axis = 1) >= 20





# user_group = np.random.randint(0, 2, (8, 6))

# group_topic = np.random.randint(0, 2, (6, 5))



# user_topic  = user_group @ group_topic

# topic_exposure = user_topic >0

# shared_topic = topic_exposure @ topic_exposure.T

# connected_user = shared_topic >= 3


# rumor_score = np.zeros((8,))

# rumor_score[[0,3]] = 1
# print(rumor_score)



# new_rumor_score = connected_user @ rumor_score

# rumor_exposure = connected_user @  new_rumor_score



# top3 = (rumor_exposure.argsort())[-3:][::-1]
# print(top3)



# arr = np.array([2,4,6,8,100])

# mean = arr.mean()

# std = arr.std()

# norm = ((arr - mean )/std)

# print(norm.mean() , norm.std())




# researcher_paper = np.random.randint(0, 2, (700, 250))
# paper_topic = np.random.randint(0, 2, (250, 50))
# journal_topic = np.random.randint(0, 2, (80, 50))


# researcher_topic  = researcher_paper @ paper_topic

# shared_topic = (researcher_topic > 0 ) @ (researcher_topic > 0  ).T

# collaborators = shared_topic >= 20
# np.fill_diagonal(collaborators , False)

# knowledge_expertise = (researcher_topic > 0 ).sum(axis = 1) 

# knowledge_gain = knowledge_expertise - shared_topic

# top5 = np.where(collaborators , knowledge_gain , -np.inf).argsort(axis = 1 )[: , -1: -6 : -1]


# topic_profile = researcher_topic[top5]
# # for every researcher extract how much each of their collaborators have contributed to each topic 


# print(topic_profile.shape)

# profile = topic_profile.mean(axis = 1)
# #for every researcher how much their collaborators have contributed to each topic collectively


# collaborators_journal = profile @ journal_topic.T

# researcher_journal = researcher_topic @ journal_topic.T

# recommended_journal =  (researcher_journal <= 8)  & (collaborators_journal >= 20)



# you didnot explicitly told what those data meant so i would assume 
# score -> how many score didi student i got in exam j
# exam_difficulty ->  it just rating from 1-10 on how difficult was the exam

# 1) scores - exam_difficulty  means  ok first lets reason it out 
# if a student scored 30 in a eaxm with difficulty rating 10 then result will contai 30 - 10 = 20 , now what does that mean wel its just how much more did the student score in a exam than its difficulty rating 


# 2) so again lets reason it through 

# scores has a shape of  (500 , 30 ) meaning 500 students and their scores in 30 exams
# exam_difficulty has a shape of (30,) difficulty rating for each exam 

# now in scores - exam_difficulty[: , None ] we are adding a new axis in the end of exam_difficulty  so it is now (30,1) now when broadcasting 
# compares dimension  30 and 1 do not match so we get shape error



# 3) 
# average = scores.mean(axis = 0 ) => (30, )

# then  relative_score = score - average[None , : ] -> this is explicit writing but just using average also gives the same result numpy handles these simple  broadcasting on its own  
 
