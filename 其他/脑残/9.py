import matplotlib.pyplot as plt
import pylab
import numpy as np
import cv2

img = plt.imread("/home/farell/PycharmProjects/pycharmTest/venv/flower.jpeg")
plt.imshow(img)
pylab.show()

filte = np.array([[1, 1, 1],
                  [1, -7, 1],
                  [1, 1, 1]])
result = cv2.filter2D(img, -1, filte)

plt.imshow(result)
pylab.show()