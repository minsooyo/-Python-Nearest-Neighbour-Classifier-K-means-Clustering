
#########################################################################################
#																						#
# 								PROGRAMMING IN DATA SCIENCE		                        #
#								ASSIGNMENT-1 B										    #
#								STUDENT ID:	u3206047										    #
#								STUDENT NAME: Minsoo Seok								    #
#								DATE OF SUBMISSION: 19 Sep 2021                               #
#								POST GRADUATE                         #
#																						#
##########################################################################################

import io_data_module as io
from io_data_module import find_nearest_neighbour
from io_data_module import calculate_distance
from io_data_module import data_average
import tkinter


###Reading the Red, blue and unknown valde form the text file
read_data =io.read_multi_dim_data('data_2c_2d.txt')
#read_data =io.read_multi_dim_data('data_4c_2d.txt')


###number of dimension
num_of_dimention= len(read_data[0])
print("Number of dimension = ", len(read_data[0]))

###Sample size
sample_size= len(read_data)
print("Number of sample size is = ", len(read_data))

###Cluster_size 
K= int(input("Input the cluster size:")) #2 or 4

threshold = 0.1 

### initial cluster_center(old_center_lists) based on K input and read_data
old_center_lists= [read_data[int(1)*(k+K)] for k in range(K)]
print("old_center_lists", old_center_lists)


###Create lists and put data into lists based on the cluster center
old_center_datas = [[] for i in range(len(old_center_lists))]
for j in read_data:
    fine_nearest = find_nearest_neighbour(j, old_center_lists)
    for i in range(len(old_center_lists)):
        if fine_nearest ==  old_center_lists[i]:
            old_center_datas[i].append(j)

####K mean algorithm
### New calcuate cluster center(average of all samples) 
### Divide into two when K=2 / K=4
new_center_1 =[0,0]
new_center_2 =[0,0]
new_center_3 =[0,0]
new_center_4 =[0,0]
if K == 2:
 for index in range(len(old_center_lists[0])):
    sum = 0
    for sample in  old_center_datas[0]:
        sum  += sample[index]
    new_center_1[index] = sum /len(old_center_datas[0])

if K == 2:
 for index in range(len(old_center_lists[0])):
    sum = 0
    for sample in  old_center_datas[1]:
        sum  += sample[index]
    new_center_2[index] = sum /len(old_center_datas[1])




if K == 4:
 for index in range(len(old_center_lists[0])):
    sum = 0
    for sample in  old_center_datas[0]:
        sum  += sample[index]
    new_center_1[index] = sum /len(old_center_datas[0])


if K == 4:
 for index in range(len(old_center_lists[0])):
    sum = 0
    for sample in  old_center_datas[1]:
        sum  += sample[index]
    new_center_2[index] = sum /len(old_center_datas[1])

if K == 4:
 for index in range(len(old_center_lists[0])):
    sum = 0
    for sample in  old_center_datas[2]:
        sum  += sample[index]
    new_center_3[index] = sum /len(old_center_datas[2])
 

if K == 4:
 for index in range(len(old_center_lists[0])):
    sum = 0
    for sample in  old_center_datas[3]:
        sum  += sample[index]
    new_center_4[index] = sum /len(old_center_datas[3])
 

###Put lists into one list for further useage
if K==2:
 new_center_lists = [new_center_1,new_center_2]
 print("new_center_lists:", new_center_lists)
elif K==4:
     new_center_lists = [new_center_1,new_center_2,new_center_3,new_center_4]
print("new_center_lists:", new_center_lists)


###Calculate sum of distance between old and new cluster centers
print(old_center_lists) # old cluster lists
print(new_center_lists) # new cluster lists

sum_dist = 0
for i in range(K):
    dist = calculate_distance(old_center_lists[i], new_center_lists[i])
    sum_dist  += dist
print(sum_dist)



###Keep modifying new cluster centers repeatly until the sum is smaller than 0.1
cluster_lists = [[] for i in range(len(old_center_lists))]

while sum_dist > threshold:
    old_center_lists = new_center_lists 
    cluster_lists = [[] for i in range(len(old_center_lists))]
    for sample in read_data:
        find_nearest = find_nearest_neighbour(sample, old_center_lists)
        for i in range(len(old_center_lists)): 
            if find_nearest == old_center_lists [i]:
                    cluster_lists[i].append(sample)
                    
    
    new_center_lists  = [[] for i in range(len(old_center_lists))]
    for i in range(len(old_center_lists)):
        new_center_lists[i] = data_average(cluster_lists[i])
        
    sum_dist = 0
    for i in range(len(old_center_lists)):
        dist = calculate_distance(old_center_lists[i], new_center_lists[i])
        sum_dist += dist
       

    print("The distance between is ", sum_dist)
else:
    print("the final cluster centre is ", old_center_lists)



### Plot the data points and the cluster centers
top = tkinter.Tk()
canvas = tkinter.Canvas(top, bg="white", height=1000, width=1000)
s = 80 #Scale factor
r = 4 # Radius
p = 180

#first center values into canvas
for i in cluster_lists[0]:
    x, y = (i[0], i[1])
    x = x*s +p
    y = y*s +p
    canvas.create_oval(x-r, y-r, x+r, y+r, outline="red", fill="red")
#second center values into canvas    
for i in cluster_lists[1]:
    x, y = (i[0], i[1])
    x = x*s +p
    y = y*s +p
    canvas.create_rectangle(x-r, y-r, x+r, y+r, outline="blue", fill="blue")

if K == 4: #third and fourth center values into canvas
 for i in cluster_lists[2]:
    x, y = (i[0], i[1])
    x = x*s +p
    y = y*s +p
    canvas.create_oval(x-r, y-r, x+r, y+r, outline="yellow", fill="yellow")
 for i in cluster_lists[3]:
    x, y = (i[0], i[1])
    x = x*s +p
    y = y*s +p
    canvas.create_rectangle(x-r, y-r, x+r, y+r, outline="green", fill="green")

# lines between datas and close center
for i in range(len(new_center_lists)):
    x1, y1 = (new_center_lists[i][0], new_center_lists[i][1])
    x1 = x1*s + p
    y1 = y1*s + p
    canvas.create_oval(x1-r, y1-r, x1+r, y1+r, outline='black', fill = 'pink')
    for j in range(len(cluster_lists[i])):
        x2, y2 = (cluster_lists[i][j][0], cluster_lists[i][j][1])
        x2 = x2*s + p
        y2 = y2*s + p
        canvas.create_line(x1,y1,x2,y2, fill='black')

 
 
canvas.pack()
top.mainloop()


############################THANK YOU############################


