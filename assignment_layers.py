imgg=imread("apeksha.jpg")
show_red=imread("apeksha.jpg")                 #reading file
show_red[:,:,1]=0                              #making other two layers 0
show_red[:,:,2]=0

show_blue=imread("apeksha.jpg")                #reading file
show_blue[:,:,0]=0                             #making other two layers 0
show_blue[:,:,1]=0

show_green=imread("apeksha.jpg")              #reading file
show_green[:,:,2]=0                           #making other two layers 0
show_green[:,:,0]=0


images=[imgg,show_red,show_blue,show_green]
heads=['Original image','Red','Blue','Green']
for i in range(4):
   plt.subplot(2,2,i+1)
   plt.imshow(images[i])
   plt.title(heads[i])

plt.show()