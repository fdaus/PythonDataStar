# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:12:31 2017

@author: firdaus afifi
"""

import numpy as np
import matplotlib.pyplot as plt


zero_2x3 = np.zeros((2,3))
print (zero_2x3)

one_2x2 = np.ones((2,2))
print(one_2x2)

three = np.full((3,3),3)
print(three)

four = np.arange(16).reshape(8,2)
print(four)

five = np.random.random((3,3))
print(five)

print(five * three)

six =np.random.randint(0,20,(3,3))
print(six)

sev = np.eye(4)
print(sev)

print(np.empty(3))


A = np.matrix([[1,2],[3,4]])
B = np.matrix([[3,4],[2,2]])
print('matrix')
print(A*B)