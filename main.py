import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

if __name__ == '__main__':
    image_path = './lena.jpg'
    target_image = cv.imread(image_path, cv.IMREAD_COLOR)
    target_image = cv.cvtColor(target_image, cv.COLOR_RGB2BGR)

    plt.imshow(target_image)
    plt.show()
#    cv.waitKey()

