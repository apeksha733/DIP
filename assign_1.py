from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
from numpy import asarray

input_image=imread("apeksha.jpg")                                        #reading image


r, g, b=input_image[: ,:,0 ],input_image[: ,: ,1], input_image[:,:,2]    #separating layers

r_const,g_const,b_const=0.33,0.33,0.33                                   #1/3 =0.33

grayscale_image=r_const * r  + g_const * g +b_const *b                   #on adding together overflow happens when>255

#task 1 Grayscale_image
#(R+G+B)/3
#--------------------------------------------------------------------------------
g_i=0.3 * r + 0.59 * g + 0.11 * b                                       #M2 using constants
#converting into grayscale (M2)

#--------------------------------------------------------------------------------
#using opencv converting rgb to binary                                 #Converting to binary using inbuilt lubb
img=cv2.imread('apeksha.jpg',2)
ret , binary_image=cv2.threshold(img,128,255,cv2.THRESH_BINARY)

#--------------------------------------------------------------------------------
#without inbuilt Library
imgg = Image.open("apeksha.jpg")                          #read image
gray = imgg.convert('L')                                  #conversion to gray scale
bin_imgg = gray.point(lambda x: 0 if x<128 else 255, '1') #conversion to binary using threshold

#--------------------------------------------------------------------------------
task_3= grayscale_image+ binary_image
# grayscale_image + binary_image        I1+I2

#-------------------------------------------------------------------------------
task_4= grayscale_image+ 20
# grayscale_image + 20                  I1+20

#Arithmetic Operations

task_5=input_image -50
task_6=input_image +50
task_7=input_image *10
task_8=input_image /50


images=[input_image,grayscale_image,g_i,binary_image,bin_imgg,task_3,task_4,task_5,task_6,task_7,task_8]
heads=['input image','grayscale M1','grayscale M2','binary inbuit lib','binary without inbuilt lib','gray+binary','gray+20','input-100','input+100','input*100','input/100']

for i in range(11):
      plt.subplot(6,2,i+1),
      plt.imshow(images[i],'gray')
      plt.title(heads[i])

plt.subplots_adjust(top=0.9,
                    wspace=0.4,
                    hspace=0.7)

plt.show()


