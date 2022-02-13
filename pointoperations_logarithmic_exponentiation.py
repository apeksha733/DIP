r=np.arange(0,256)
c1=255/(np.log(1+255))
y1=c1*np.log(1+r)


img=imread("apeksha.jpg")       #reading img
c1=255/(np.log(1+255))          #log transformation
log_img=c1*np.log(img+1)
log_img=np.array(log_img,dtype=np.uint8)

plt.subplot(1,3,1)
plt.imshow(img,cmap='gray')
plt.title('original')
plt.subplot(1,3,2)
plt.imshow(log_img,cmap='gray')
plt.title('logarithmic')

c2=255/(np.log(1+255))
y2=np.exp(r)**(1/c2)-1

exp_img=np.exp(img**1/c2)-1
exp_img=np.array(exp_img,dtype=np.uint8)
plt.subplot(1,3,3)
plt.imshow(exp_img,cmap='gray')
plt.title('exponentiation')

#plt.plot(r,y1)
#plt.plot(r,y2)

plt.show()