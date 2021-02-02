#0~100의 성분을 갖는 행렬에서 20보다 크고 55보다 작은 값은 2 나머지 값은 0으로 출력되는 arrray를 만드시오
import numpy as np
A = np.arange(0,100)
B = np.logical_and((A>20),(A<55))
print(2*B)
B = 2*(A>20)*(A<55)
print(B)

#B를 가지고 A값이 3의 배수일때만 B에다가 A를 곱하시오
condition = (A%3 == 0) #A에서 3의 배수일때만 True값 준다.
print(condition)
B[condition] *= A[condition]
print(B)

result = np.genfromtxt('test0125.txt') #txt파일을 np.array값으로 가지게됨
print(result)
import matplotlib.pyplot as plt
#print(plt.plot(result))
x = np.arange(0,3*np.pi, 0.1) # 0부터 3pi까지 0.1씩 차이를 갖는 array 
y = np.sin(x)

plt.plot(x,y)
plt.show()