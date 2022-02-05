# Read the image and converting in grayscale
img = cv2.imread("apeksha.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
         lst.append(np.binary_repr(img[i][j] ,width=8)) # width = no. of bits

#obtaining bit planes
eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(img.shape[0],img.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64).reshape(img.shape[0],img.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32).reshape(img.shape[0],img.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(img.shape[0],img.shape[1])
four_bit_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8).reshape(img.shape[0],img.shape[1])
three_bit_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4).reshape(img.shape[0],img.shape[1])
two_bit_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2).reshape(img.shape[0],img.shape[1])
one_bit_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1).reshape(img.shape[0],img.shape[1])

images=[eight_bit_img,seven_bit_img,six_bit_img,five_bit_img,four_bit_img,three_bit_img,two_bit_img,one_bit_img]
#storing and plotting image

heads=['7th bit','6th bit','5th bit','4th bit','3rd bit','2nd bit','1st bit','0th bit']
for i in range(8):
    plt.subplot(4,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(heads[i])
plt.subplots_adjust(top=0.9,
                    wspace=0.4,
                    hspace=0.7)
plt.show()