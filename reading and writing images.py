# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 23:35:09 2021

@author: HP
"""

import cv2 #importing opencv library

print("Package Imported")

img = cv2.imread("lenna.png") #reads image given path

cv2.imshow('Output',img) #shows image stored above/ the first parameter is the name of output window

cv2.waitKey(0) #Adds delay in miliseconds - (0) means infine delay
cv2.destroyAllWindows() #to remove/delete created GUI windows