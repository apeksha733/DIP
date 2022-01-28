arr=np.array([[52,55,61,59,79,61,76,61],
              [62,59,55,104,94,85,59,71],
              [63,65,66,113,144,104,63,72],
              [64,70,70,126,154,109,71,69],
              [67,73,68,106,122,88,68,68],
              [68,79,60,70,77,66,58,75],
              [69,85,64,58,55,61,65,83],
              [70,87,69,68,65,73,78,90]])

data = Image.fromarray(arr)
plt.imshow(data)
plt.show()
#----------------------------------------------------------------

H=np.zeros(shape=(256,1))
for i in range(8):
    for j in range(8):
        k=arr[i,j]
        H[k,0]=H[k,0]+1

plt.plot(H)
plt.show()
#---------------------------------------------------------------

x=H.reshape(1,256)
y=np.array([])

y=np.append(y,x[0,0])

for i in range(255):
    k=x[0,i+1]+y[i]
    y=np.append(y,k)

y=np.round((y/64)*255)

for i in range (8):
    for j in range (8):
        k=arr[i,j]
        arr[i,j]=y[k]

print(arr)
data2 = Image.fromarray(arr)
plt.imshow(data2)
plt.show()

#------------------------------------------

H1=np.zeros(shape=(256,1))
for i in range(8):
    for j in range(8):
        k=arr[i,j]
        H1[k,0]=H1[k,0]+1

plt.plot(H1)
plt.show()
