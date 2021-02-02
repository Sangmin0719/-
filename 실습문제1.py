#numb = int(input('Please enter the integer: '))

#if numb == 0:
#    print('integer is zero')
#elif numb <= -1:
#    print('integer is negative')
#else:
#    if (numb%2 == 0):
#        print('integer is even integer')
#    else: 
#        print('integer is odd integer')

#def fun():
#    if (numb > 0):
#        print('양의 정수입니다.')
#        if (numb%2): # numb가 홀수 일겨우 나머지 1 = ture, 짝수일 경우 0 = False
#            print ('홀수 입니다.')
#    elif (numb == 0):
#        print ('0입니다.')
#    else:
#        print ('음의 정수 입니다.') 

#for a in range(-10,11):
#    print(a) 
#    fun(a)

from abc import abstractproperty


A = [0,1,4,3,7,2,3]

def bublesort(target):
    N = len(target)
    result = target.copy()
    for M in range(N,2,-1): #??
        for i in range(N-1):
            if (result[i] > result[i+1]):
                result[i], result[i+1] = result[i+1], result[i]
    return result
bublesort(A)

def bublesort(target):
    ischanged = False
    N = len(target)
    result = target.copy()
    for M in range(N,2,-1): #??
        print(M)
        for i in range(N-1):
            if (result[i] > result[i+1]):
                result[i], result[i+1] = result[i+1], result[i]
                ischanged = True
        if not ischanged:
            break
    return result

bublesort(A)

A.sort()
print (A)

a = [1 , 3, 0, 2, 8, 0, 7, 0, 4]
def f(array, order, value: int):
    if array[order] != 0:
        pass
    elif value in array: 
        pass
    else:
        array[order] = value
    return array
print(f(a,2,5))

#order = int(input('Please enter the integer'))
#value = int(input('Please enter the integer'))

#Try and Except 
#
#del a
#print (a)
try:
    print (aa)
except:
    print('a가 정의 되지 않았습니다.')
    aa = 1 
print(aa)

import numpy as np
from numpy import * 

try:
    from numpy import sqrt
except:
    from math import sqrt
def root(number):
    return sqrt(number)

#root(10)


A = ['Python', '5', 'class', '10', 'funny', '20']
def func(A):
    b = [] #출력변수
    for var in A:
        try:
            tmp = float(var)
            b += [tmp]
        except:
            pass    
    return b
func(A)