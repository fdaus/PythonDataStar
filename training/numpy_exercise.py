# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:17:20 2017

@author: firdaus afifi
"""
import numpy as np
import matplotlib.pyplot as plt



#1-Create a 3x3 matrix with values ranging from 0 to 8

A = np.arange(0,9).reshape(3,3)
A = np.matrix(A)

print(A)

#2-Create a 10x10 array with random values and find the minimum and maximum values

B = np.random.randint(0,20,(10,10))
print(B.shape)

print('min', np.min(B))
print('min', np.max(B))

#3-Create a 8x8 matrix and fill it with a checkerboard pattern
x = np.array([[0,1],[0,1]])
C = np.repeat(x,2,axis=1)

print(C)


#4-Create random vector of size 10 and replace the maximum value by 0

D = np.random.randint(0,10,(10))
D[D == np.max(D)]=0
print(D)
#5-Create a  4∗44∗4  identity matrix.

E = np.identity(4)
print(E)
#6-Generate the 2D array

F = np.array([[1,2],[3,4]])
print(F)
#7-Generate a random  4×4×44×4×4  array of Gaussianly distributed numbers.
#8-Generate n evenly spaced intervals between 0. and 1.
#9-Create a vector and then reverse the vector (first element becomes last)





np.r_









def build_checkerboard(w, h) :
      re = np.r_[ w*[0,1] ]              # even-numbered rows
      ro = np.r_[ w*[1,0] ]              # odd-numbered rows
      return np.row_stack(h*(re, ro))

c = build_checkerboard(4, 4)

#print(c)


#fig, ax = plt.subplots()
#ax.imshow(c, cmap=plt.cm.gray, interpolation='nearest')
#plt.show()