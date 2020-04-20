import math
import os
import random
import re
import sys

n=10
queries=[
    [1,5,3],
    [4,8,7],
    [6,9,1]
]
print(len(queries))

def arrayManipulation(n, queries):
    arr=[0]*(n+1)
    for i in range(len(queries)):
        a=queries[i][0]
        b=queries[i][1]
        k=queries[i][2]
        arr[a-1]+=k
        arr[b]-=k
    sum=0
    maxx= -(2 **31)
    for i in range(n+1):
        sum+=arr[i]
        maxx=max(maxx,sum)
    
    return maxx

print(arrayManipulation(n,queries))

