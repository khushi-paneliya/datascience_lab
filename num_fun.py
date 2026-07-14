import sys
import numpy as np
arr=np.array([1,4,9,16])
#universal function
print (np.sqrt(arr))
print (np.square(arr))
print (np.sin(arr))
print (np.cos(arr))

#Aggregate functions

arr=np.array([10,20,30,40,50])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))