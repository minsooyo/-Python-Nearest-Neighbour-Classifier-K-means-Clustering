#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:28:43 2021

@author: soo
"""
def read_multi_dim_data(filename):

   """

   Reads a multi-dimensional data from a file.

   """

   ### final data from file

   dataset = []

   try:

       with open(filename, 'r') as file:

           ##Read each line one at a time

           for line in file:

               ##Checking for the end of the file

               if line.strip() == '':

                   break

 

               ##read dynacic coordinate

               read_line = [float(x) for x in line.strip().split()]

               read_line = tuple(read_line)

 

               dataset.append(read_line)

   except FileNotFoundError:

       print("File not found")


 

   return dataset





        
#calculate_distance
def calculate_distance(p1, p2):
    d = 0
    for i in range(len(p1)):
        d += (p2[i] - p1[i])* (p2[i] - p1[i])
    d= d**0.5
    return d


#find_nearest_neighbor
def find_nearest_neighbour(unknown_sample, data_list):
      shortest_distance = 10000000
      nearest_sample = ()
      for sample in data_list:
          dist= calculate_distance(unknown_sample, sample)
          if  shortest_distance > dist:
              shortest_distance = dist
              nearest_sample  = sample
      return   nearest_sample 
        

    
        # data_average
def data_average(data_list):
    data_centre = []
    for index in range(len(data_list[0])):
        sum=0
        for sample in data_list:
            sum += sample[index]
        data_centre.append(sum / len(data_list))
    return data_centre
        
        


        

