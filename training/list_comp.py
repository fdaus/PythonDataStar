# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:33:14 2017

@author: firdaus afifi
"""

country = ['India', 'Pakistan', 'Nepal', 'Bhutan'] 
capital = ['New Delhi', 'Islamabad','Kathmandu', 'Thimphu'] 
d = {} 
for i in range(len(country)): 
    d[country[i]] = capital[i]
    
print(d)
print()
e = {country[i]:capital[i] for i in range(len(country))}

print(e)
print()

f = {k: v for k in country for v in capital}

print(f)