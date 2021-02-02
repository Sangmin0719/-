#sum1 = 0
#for i in range(11,101):
#    i1 = (i%10)*10 + int(i/10)
#    if i1 % i == 0:
#        print(i)
#        sum1 += i
#print(sum1)       
#sum0 = 0
#for N in range(11,100): #조교님 방법142857은 신기한 숫자
#    Nstr = str(N)
#    Nrot = int( Nstr[-1] + Nstr[:-1])
#    if Nrot%N == 0:
#        print(N)
#        sum0 += N
#print('sum is', sum0)

#def Primenumber(k):
#    result = 0
#    for n1 in range(2,k):
#        for n2 in range(n1):
#            if n1%n2 != 0:
#                print(n1)
#                result += n1

#def Primenumber(a):
#    result = 0
#    while a > 0:
#        for i in range(1,1000):
#            for j in (1,i):
#                if i%j == 0:
#                    print('a')
#                else:
#                    print(i)
#                    a = a - 1
#
from math import floor


n = 7
from math import ceil #올림, #floor 내림

def CheckPrime(n):# 소수면 1을 리턴, 소수가 아니면 0리턴
    lastnumber = ceil(n/2) +1
    flag = 1 #1:소수, 0: 소수가 아닌 숫자
    for i in range(2,lastnumber): # 마지막 경계값으로 나와야 적어도 1이 나온다 
        if n % i == 0:
            flag = 0
            break
    return flag
print(CheckPrime(10))


#숫자 N이 주어지면, n<N 소수를 모두 출력하는 함수
def Primenumber(k):
    for n1 in range(1,k):
        for n2 in range(2,n1):
            if n1%n2 == 0:
               pass 
            else:
                return n1
            
Primenumber(10)
N = int(input('Please enter last boundary condition number: '))
for n1 in range(2,N):
    if CheckPrime(n1) == 1:  #if CheckPrime{n1}
        print(n1)

def FindPrime2 (N):
    prime = []
    n = 2
    while len(prime) < N:
        if CheckPrime(n):
            prime += [n]
        n += 1
    return prime[-1]# N번째 소수 

print(FindPrime2(N))