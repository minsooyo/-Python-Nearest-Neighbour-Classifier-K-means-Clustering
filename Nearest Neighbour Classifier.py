
#########################################################################################
#																						#
# 								PROGRAMMING IN DATA SCIENCE		                        #
#								ASSIGNMENT-1 A								    #
#								STUDENT ID:	u3206047										    #
#								STUDENT NAME: Minsoo Seok								    #
#								DATE OF SUBMISSION: 19 Sep 2021                               #
#								POST GRADUATE                         #
#																						#
##########################################################################################

import io_data_module as io
from io_data_module import find_nearest_neighbour
from io_data_module import calculate_distance
import tkinter 

red_data =  ["datasets/red_2d.txt","datasets/red_4d.txt","datasets/red_8d.txt"]
blue_data =  ["datasets/blue_2d.txt","datasets/blue_4d.txt","datasets/blue_8d.txt"]
unknown_data =  ["datasets/unknown_2d.txt","datasets/unknown_4d.txt","datasets/unknown_8d.txt"]

red = None
blue = None
unknown = None

###Reading the dataset
while True:
	try:
		select_dimension = int(input("Select the Dimension for the Red and blue dataset (2,4,8):"))
		if select_dimension == 2:
			red = io.read_multi_dim_data(red_data[0])
			blue = io.read_multi_dim_data(blue_data[0])
			unknown= io.read_multi_dim_data(unknown_data[0])
			break


		elif select_dimension == 4:
			red = io.read_multi_dim_data(red_data[1])
			blue = io.read_multi_dim_data(blue_data[1])
			unknown = io.read_multi_dim_data(unknown_data[1])
			break

		elif select_dimension == 8:
			red = io.read_multi_dim_data(red_data[2])
			blue = io.read_multi_dim_data(blue_data[2])
			unknown = io.read_multi_dim_data(unknown_data[2])
			break

		else:
			raise ValueError

	except ValueError:
		print("Please enter a valid number")




###Calculate distances between unknown_point and all datas(red/blue)
unknown_point = unknown[0] #any number 0 ~ 19

min_distance_from_red = find_nearest_neighbour(unknown_point,red)
distance_red_unknown = calculate_distance(min_distance_from_red, unknown[0])


min_distance_from_blue = find_nearest_neighbour(unknown_point,blue)
distance_blue_unknown = calculate_distance(min_distance_from_blue, unknown[0])

###Compare the distance between unknown_point to (red/blue)
if(distance_red_unknown > distance_blue_unknown):
    print(f"The unknwon_point {unknown_point} is blue")
else:
    print(f"The unknwon_point {unknown_point} is red")


###Combine red and blue dataset for further usage
combine = red+blue

###Define 4 important lists
unknown_near_red = [] #unknown datas that close to the red 
unknown_near_blue = [] #unknown datas that close to the blue
red_near_unknown = []  #red datas that close to the unknown data
blue_near_unknown = [] #blue datas that close to the unknown data

###Append values into above lists
for i in unknown:
    nearest_combine =find_nearest_neighbour(i, combine)
    if nearest_combine in red:
        unknown_near_red.append(i)
        red_near_unknown.append(nearest_combine)
    elif nearest_combine in blue:
        unknown_near_blue.append(i)
        blue_near_unknown.append(nearest_combine)

###Label output on screen and save as file ('classified_data.txt')
classified_data = open('classified_data.txt', 'w')
for i in unknown:
    output = str(i[0:])
    if i in unknown_near_red:
        output = (output[1:-1]+ ' RED')
    if i in unknown_near_blue:
        output = (output[1:-1]+ ' BLUE')
    print(output)
    classified_data.write(output + "\n")
classified_data.close()


###Output on canvas 
top = tkinter .Tk() #change 
canvas = tkinter.Canvas(top, bg= "white", height = 1000, width = 1000)
s = 80
r = 4
p = 180

#red dataset into plot 
for i in red:
    x = i[0]
    y = i[1]
    x = x*s+p
    y = y*s+p
    canvas.create_oval(x-r, y-r, x+r,y+r, outline="red", fill="red") 
    
#blue dataset into plot
for i in blue:
    x = i[0]
    y = i[1]
    x = x*s+p
    y = y*s+p
    canvas.create_oval(x-r, y-r, x+r,y+r, outline="blue", fill="blue") 


#unknown samples closed to red data into plot and add line to see crearly
for i,j in zip(unknown_near_red, red_near_unknown):
    x = i[0]
    y = i[1]
    x = x*s+p
    y = y*s+p 
    x2 = j[0]
    y2 = j[1]
    x2 = x2*s+p
    y2 = y2*s+p
    canvas.create_oval(x-r, y-r, x+r, y+r, outline = "red", fill="white")
    canvas.create_line(x, y, x2, y2,fill="red")
    
#unknown samples closed to blue data into plot and add line to see crearly
for i,j in zip(unknown_near_blue, blue_near_unknown):
    x = i[0]
    y = i[1]
    x = x*s+p
    y = y*s+p 
    x2 = j[0]
    y2 = j[1]
    x2 = x2*s+p
    y2 = y2*s+p
    canvas.create_oval(x-r, y-r, x+r, y+r, outline = "blue", fill="white")
    canvas.create_line(x, y, x2, y2,fill="blue")
    
canvas.pack()
top.mainloop()
    

############################THANK YOU############################

    
    
    
    
    
    
    
    
    
    
    
    