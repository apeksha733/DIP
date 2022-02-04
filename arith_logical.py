image1 = cv2.imread('im1.jpg')
image2 = cv2.imread('im22.jpg')

add = cv2.add(image1,image2)
sub = cv2.subtract(image1, image2)

bitwiseand = cv2.bitwise_and(image1,image2,mask=None)
bitwiseor = cv2.bitwise_or(image1,image2,mask=None)
bitwisenot = cv2.bitwise_not(image1)
bitwisexor = cv2.bitwise_xor(image1,image2,mask=None)



images=[image1,image2,add,sub,bitwiseand,bitwiseor,bitwisenot,bitwisexor]
heads=['image1','image2','add','sub','bitwiseand','bitwiseor','bitwisenot','bitwisexor']
for i in range(8):
    plt.subplot(4,2,i+1)
    plt.imshow(images[i])
    plt.title(heads[i])
plt.subplots_adjust(top=0.9,
                    wspace=0.4,
                    hspace=0.7)
plt.show()
