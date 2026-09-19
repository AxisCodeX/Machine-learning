import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


x = np.linspace(-5,5,50)
y = np.linspace(-5,5,50)

X,Y = np.meshgrid(x,y)
Z = X**2 + X**2
print(X)
print(Y)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(X, Y, Z)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()