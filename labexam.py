# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,7,8]])
print("Original Array \n",a)
print("Display all elements excluding the first row")
print(a[1:])
print("Display the 3rd and 4th element of 1st row")
print(a[0,2],a[0,3])

OUTPUT

Original Array 
 [[1 2 3 4]
 [5 6 7 8]
 [9 1 2 3]
 [4 5 7 8]]
Display all elements excluding the first row
[[5 6 7 8]
 [9 1 2 3]
 [4 5 7 8]]
Display the 3rd and 4th element of 1st row
3 4
