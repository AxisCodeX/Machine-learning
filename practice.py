import cv2
import numpy as np


image = cv2.imread("cat.jpg")

image = cv2.resize(image , (500 , 500))
print(image.shape)

image[image[: , :  , 0] > 150] = [255 , 0 ,0]
image[image[: ,: ,1] < 80] = [0 , 255, 0]
image[image[: , : ,2] < 100] = [0 ,0 ,255]



cv2.imshow("image", image)

while True:
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
