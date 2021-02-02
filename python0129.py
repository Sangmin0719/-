#-*- coding: utf-8 -*-
import random
import numpy as np
from numpy.core.numeric import count_nonzero
# A= [[1,2,3],[0,1,2],[1,2,3]]
# c = np.array[A]

# print(c)
# np.sin(1)
# print(np.sin(1))
# import random
# print(random.random()) # random function retrun randomnumber in 0~1
# print(round(1.96))# 반올림
# print(round(1.9615,3))#소수점 몇번째 까지 반올림하고 출력
# print(random.randint(1,5)) #1~5까지 

card = input(str('가위~ 바위~ 보~:' ))

while card != '가위' and card != '바위' and card != '보':
    print('가위 바위 보 중 하나를 내셔야합니다!^^')
    card = input(str('가위~ 바위~ 보~:' ))
rand = random.randint(1,3) #가위 1, 바위 2, 보 3 
if card == '가위' : 
    if rand == 1: 
        print('가위,', '비겼다.')
    elif rand == 2: 
        print('바위, 내가 이겼다 ㅋㅋ' )
    else:
        print('보, 내가 졌다 ㅠ')
if card == '바위' : 
    if rand == 1: 
        print('가위,', '졌다ㅠ.')
    elif rand == 2: 
        print('바위, 비겼다' )
    else:
        print('보, 내가 이겼네 ㅋㅋ')
if card == '보' : 
    if rand == 1: 
        print('가위,', '이겼다.')
    elif rand == 2: 
        print('바위, 내가 졌넹 ㅠ' )
    else:
        print('보, 비겼다ㅋㅋ')
morse = np.genfromtxt('morse1.txt',dtype = 'str')#,dtype = 'str')   #가져올떄 숫자로 가져옴      
print(morse, type(morse))

#open('morse.txt', 'rt', encoding='UTF8')

# alp ='A'
# alp_i = np.where(morse[:,0]==alp)[0][0] # alpdp에 해당하는 
# print(np.where(morse[:,0]==alp)[0][0])
# print(np.where(morse[:,0]==alp)[0])
# print(morse[alp_i, 1]) # morse에서 alp_i에 해당하는 행에서 1(2)번쟤행
#numpy.where(조건) ->조건을 만족하는 튜플을 줌 (array([1],))
# alp = input(str('Please enter the sentence :'))
# alp = alp.upper()# 대문자로 바꿔주는거임
# alp_i = np.where(morse[:,0]==alp)[0][0]
# print(morse[alp_i, 1])
# for i in len(alp):
#     a = alp[i]
#     a = np.where(morse[:,0]==alp)[0][0]
#     print(morse[a,1], end=',')


word = 'apple'
for alp in word:
    alp = alp.upper()
    alp_i = np.where(morse[:,0]==alp)[0][0]

    print(morse[alp_i,1])

word = 'apple'
result = ''
for alp in word:
    alp = alp.upper()
    alp_i = np.where(morse[:,0]==alp)[0][0]
    result += morse[alp_i,1]+' ' 
print(result)

# word1 = input('please enter the word: ')
# result = ''
# for alp in word1:
#     alp = alp.upper()
#     alp_i = np.where(morse[:,0]==alp)[0][0]
#     result += morse[alp_i,1]+' ' 
# print(result)

# sentense = input('please enter the sentense:')
# result = ''
# for alp in sentense:
#     if alp == ' ':
#         result += '  '
#     else:    
#         alp = alp.upper()
#         alp_i = np.where(morse[:,0]==alp)[0][0]
#         result += morse[alp_i,1]+' ' 
# print(result)

for i in range(10):
    a = i
    print('(',random.random(),",",random.random(),')')
N = 10
x = []
y = []
count = 0
while count < N:
    count += 1
    x.append(random.random())
    y.append(random.random())
print(x)
print(y)

points = np.random.random((N,2))
print(points)
x = points[:0]
y = points[:0]

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.scatter(x,y)
plt.show()


