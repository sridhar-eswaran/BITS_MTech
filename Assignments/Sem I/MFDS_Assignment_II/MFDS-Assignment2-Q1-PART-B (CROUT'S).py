#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import copy
import math
import time
from cmath import e

A = np.random.uniform(0, 9,  size=(10,10))
A = A*10000//1/10000
b = np.random.uniform(0, 9,  size=(10,1))
b = b*10000//1/10000


# In[2]:


def forward_sub(L, b):
    """x = forward_sub(L, b) is the solution to L x = b
       L must be a lower-triangular matrix
       b must be a vector of the same leading dimension as L
    """
    n = L.shape[0]
    x = np.zeros(n)
    for i in range(n):
        tmp = b[i]
        for j in range(i-1):
            tmp -= L[i,j] * x[j]
        x[i] = tmp / L[i,i]
    return x


# In[3]:


def back_sub(U, b):
    """x = back_sub(U, b) is the solution to U x = b
       U must be an upper-triangular matrix
       b must be a vector of the same leading dimension as U
    """
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        tmp = b[i]
        for j in range(i+1, n):
            tmp -= U[i,j] * x[j]
        x[i] = tmp / U[i,i]
    return x


# In[4]:


def lu_solve(L, U, b):
    """x = lu_solve(L, U, b) is the solution to L U x = b
       L must be a lower-triangular matrix
       U must be an upper-triangular matrix of the same size as L
       b must be a vector of the same leading dimension as L
    """
    forward_sub_start_time = time.time()   
    y = forward_sub(L, b)
    print("Total time taken in forward substitution in seconds", time.time() - forward_sub_start_time)
    back_sub_start_time = time.time()
    x = back_sub(U, y)
    print("Total time taken in backward substitution in seconds ", time.time() - back_sub_start_time)
    return x


# In[5]:


def crout2(A): 
    n = len(A)
    L = [[0] * n for i in range(n)]
    U = [[0] * n for i in range(n)]
    for j in range(n):
        U[j][j] = 1                     # set the j,j-th entry of U to 1
        for i in range(j, n):          # starting at L[j][j], solve j-th column of L
            alpha = float(A[i][j])
            for k in range(j):
                alpha -= L[i][k]*U[k][j]
            L[i][j] = alpha
        for i in range(j+1, n):        # starting at U[j][j+1], solve j-th row of U
            tempU = float(A[j][i])
            for k in range(j):
                tempU -= L[j][k]*U[k][i]
            if int(L[j][j]) == 0:
                L[j][j] = e-40
            U[j][i] = tempU/L[j][j]
    return [L, U]


# In[6]:
A = np.random.uniform(0, 9,  size=(3,3))
#A = A*10000//1/10000
b = np.random.uniform(0, 9,  size=(2,2))
b = b*10000//1/10000

#def crout(A):
n = len(A)
L = [[0] * n for i in range(n)]
U = [[0] * n for i in range(n)]
for i in range(n):
    L[i][0] = A[i][0]
    U[i][i] = 1
for j in range(1,n):
    U[0][j] = A[0][j]/L[0][0]
del i,j

for i in range(1,n):  #i=1
    for j in range(1,i): # 1,1
        L[i][j] = A[i][j] - L[i][0:j-1] * U[0:j-1][j]
        print(' First loop i=',i,' ','j=',j)
    for j in range(i+1,n):
        print(j)
        U[i][j] = (A[i][j] - L[i][0:i-1] * U[0:i-1][j])/L[i][i]
        print(' Second Loop i=', i, ' ', 'j=', j)
            
    #return [L, U]


# In[7]:


crouts_start_time = time.time()     
X = crout(A);
print("Total time taken in LU decomposition for An*n matrix in seconds", time.time() - crouts_start_time)
#print(X[0])    
#print(X[1])
forward_backward_start_time = time.time()     
lu_solve(np.block(X[0]),np.block(X[1]),np.array(b))
print("Total time taken in forward and backward substitution in seconds", time.time() - forward_backward_start_time)


# In[ ]:



