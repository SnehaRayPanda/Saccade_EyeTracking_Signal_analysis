# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:58:51 2022

@author: Sneha Ray
"""

import pickle as pck
import os
#%% Task to DO
#     To open the file
#     import pickle as pck
#     openfile = open("data_exam.pck", "rb")
#	  A=pck.load(openfile)
#     openfile.close()

#	At that point, you have a variable A containing all the needed data 
#   (you will see that the format of the dictionary should be familiar).
#	Those are eye tracking movements. I want you to focus on the signals l_x and l_y. 
#   The big shifts in the position correspond to saccades EYE Signal.
#   Using these data, I expect from you that:

# 1.	You filter the data between 21 and 32 seconds.
# 2.    You plot the filtered and the raw data on the same graph (so I can compare)
# 3. 	You do a 2D plot of the data
#		You do a plot that represents the duration of each saccade as a function of their amplitude
#       (within 37 and 48 seconds).
#		This means that you will have to detect the saccades! Manual is OK, 
#       using a script is WAAAAAYYYY better.
# Put comments in the file to explain what you are doing. DL: January 31th 2022
#%% Go to the directory where data is there and read the data
path='C:/Users/bkbme/Desktop/Sneha_program/CompNeuro/'
os.chdir(path)			
openfile = open("data_exam.pck", "rb")
A=pck.load(openfile)
openfile.close()
#%% assign the 1_x and l_y signal to data_l_x and data_l_y variable respectively
data_l_x =A[trial0]
