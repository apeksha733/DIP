image = cv2.imread("Lenna.png")
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Sobel Edge detection
sobelx = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)


#Robert Edge detection
roberts_cross_v = np.array([[1, 0],
                            [0, -1]])

roberts_cross_h = np.array([[0, 1],
                            [-1, 0]])


img1 = cv2.imread("Lenna.png", 0).astype('float64')

vertical = ndimage.convolve(img1, roberts_cross_v)
horizontal = ndimage.convolve(img1, roberts_cross_h)

edged_img = np.sqrt(np.square(horizontal) + np.square(vertical))
#Prewitt Edge Detection

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gray, -1, kernelx)
img_prewitty = cv2.filter2D(img_gray, -1, kernely)
img_prewittxy=img_prewittx + img_prewitty

images=[img_gray,sobelx,sobely,sobelxy,edged_img,img_prewittx,img_prewitty,img_prewittxy]
heads=['original gray','sobelx','sobely','sobelxy','Robert','prewittx','prewitty','prewittxy']

for i in range(8):
       plt.subplot(4,2,i+1),
       plt.imshow(images[i],'gray')
       plt.title(heads[i])
plt.subplots_adjust(top=0.9,
                    wspace=0.4,
                    hspace=0.7)
plt.show()