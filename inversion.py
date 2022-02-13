from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
from numpy import asarray
import re
import collections

image_src = imread("apeksha.jpg")
image_i = 255 - image_src                   #inversion

cmap_val = 'gray'
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 20))

ax1.axis("off")
ax1.title.set_text('Original')

ax2.axis("off")
ax2.title.set_text("Inverted")

ax1.imshow(image_src, cmap=cmap_val)
ax2.imshow(image_i, cmap=cmap_val)                  #plot

plt.show()
