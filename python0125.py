#for i in range(7,0,-1): #총길이, 어디서부터 시작, 얼마만큼 줄어드는지
#    print ('#'*i)

slen = 3
for j in range(slen):
    print()  
    for i in range (slen):
        print('i, j',i,j)

# amat = [[a11, a12, a13],
#         [a21, a22, a23]
#         [a31, a32, a33]]

ndim = 5
for j in range(1, ndim + 1):
    row = []
    for i in range(1, ndim+1):
        row.append(i)

f = lambda x : x**2 #same as def f(x): return x**2
print(f(4))
flam = lambda x,y : x*y #문자 두개도 가능
# object 객체, 펫말? 가르키는 기능, 다른 내용을 가르키는 애들?

alist = [1,5,3,2,8,4]
alist.sort(reverse=True) # 역순으로
print(alist)
alist.sort() #순서대로 베열 작은차순
print(alist)
word=['j','o','s','a','n','g','m','i','n']
word.sort() #알페벳 순으로 정렬
print(word)

ord('a')

from pickle import TRUE
from random import randrange
import numpy as np

# class 사람():
#     이름 =
#     나이 =
#     def 인사:
#         self.손들기() 

A = np.array([1,2,3,4,5])
B = np.array([1,0,2,1,0])
A + 2
print(A)
print(A==B) # A와 B의 성분들이 같은지 아닌지를 bool로 줌
print(A>B) #각 성분들의 대소 비교를 bool로 줌   

A1 = np.array([False, True, False])
B1 = np.array([True, False, True])
print(np.logical_and(A1,B1)) #요소들이 불리안일경우에는 logical_and or logical_or
print(A1*B1) #and는 단순히 곱해주면 됨 ㅋㅋ

A2 = np.array([[1,2,3,4],[0,3,0,4]])#Print 될때는 자동적으로 슬라이싱됨
print(A2)
print(A2[1,1:4]) # A2의 1행의 1~4번째 성분을 가져오라

condition = np.array([True, False, True, False])
A3 = np.array([3,0,2,7])
print(A3[condition]) #A3에서 condition에 맞는에만 출력
print(A2[1,condition])# A2의 1행에서 condition에 맞는 에만 출력

import time
# time_start = time.time()
# A = np.zeros([2000,2000])#0으로 구성된 array
# for i in range(2000):
#     for j in range(2000):
#         A[i,j] = A[i,j] + 1
# time_finish = time.time()
# print(time_finish - time_start)# for로 하면 오래걸림 약 4.6초

# time_start = time.time()
# A = np.zeros((2000, 2000))
# A = A + np.ones((2000, 2000))
# time_finish = time.time()

# print(time_finish - time_start) # 0.036초  for문보다 약 100배 빠름

