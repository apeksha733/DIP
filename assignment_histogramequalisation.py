arr=np.array([[52,55,61,59,79,61,76,61],
              [62,59,55,104,94,85,59,71],
              [63,65,66,113,144,104,63,72],
              [64,70,70,126,154,109,71,69],
              [67,73,68,106,122,88,68,68],
              [68,79,60,70,77,66,58,75],
              [69,85,64,58,55,61,65,83],
              [70,87,69,68,65,73,78,90]])

data = Image.fromarray(arr)                                  #obtaining image from matrix
plt.imshow(data)                                             #showing image
plt.show()
#----------------------------------------------------------------

hist,bins = np.histogram(arr.flatten(),256,[0,256])          #plotting histogram for original image

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')


plt.hist(arr.flatten(),256,[0,256], color = 'r')             #plotting
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
#----------------------------------------------------------------

H=np.zeros(shape=(256,1))
for i in range(8):
    for j in range(8):
        k=arr[i,j]
        H[k,0]=H[k,0]+1                                    #plotting

plt.plot(H)
plt.show()
#---------------------------------------------------------------

x=H.reshape(1,256)
y=np.array([])

y=np.append(y,x[0,0])

for i in range(255):
    k=x[0,i+1]+y[i]
    y=np.append(y,k)

y=np.round((y/64)*255)                                  #equation for histogram equalisation

for i in range (8):
    for j in range (8):
        k=arr[i,j]
        arr[i,j]=y[k]

print(arr)
data2 = Image.fromarray(arr)                             #getting image from array
plt.imshow(data2)
plt.show()

#------------------------------------------------------------
hist,bins = np.histogram(arr.flatten(),256,[0,256])       #Histogram equalisation

cdf = hist.cumsum()                                       #obtaining cdf using inbuilt function
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')


plt.hist(arr.flatten(),256,[0,256], color = 'r')          #plotting graph
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

#-----------------------------------------------------------------------------


H1=np.zeros(shape=(256,1))
for i in range(8):
    for j in range(8):
        k=arr[i,j]
        H1[k,0]=H1[k,0]+1

plt.plot(H1)
plt.show()