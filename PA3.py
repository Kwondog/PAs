# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:16:26 2024

@author: LAKwon
"""

import numpy as np

#question 4

def fx():
    return np.poly1d([2, 3, 0, 1])
    
def f(x):
    return np.polyval(fx(), x)
    
# fx()
f(2)
#%%
def fx():
    q5 = np.poly1d([1, 0, 1])
    q5der = np.polyder(q5, 1)
    print(q5der)
    return np.polyval(q5der, 1)
fx()
#%%
#Part II
print("Enter an equation's coefficients separated by a comma")
getEquation = input("example 4,0,2,1:")
equationList = list(getEquation.split(","))
for i in range(len(equationList)):
    equationList[i] = int(equationList[i])

polynomial = np.poly1d(equationList)
x = int(input("enter a number to start the Newtons equation"))

def Newton(equation, x, count):
    newt1 = x - np.polyval(equation, x)/np.polyval(np.polyder(equation, 1), x)
    newt2 = x-1 - np.polyval(equation, x-1)/np.polyval(np.polyder(equation, 1), x-1)
    if f"{newt1:.3}" == f"{newt2:.3}" and count > 2:
        return print("The roots of the equation are", np.roots(equation))
    print("x_%d = %.3f" %(count, newt1))
    return Newton(equation, x + 1, count + 1)
    
        

    
Newton(polynomial, x, 1)