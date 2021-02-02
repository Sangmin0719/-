#s1  = '안녕하세요', s2 = '여러분', s3 = '즐거운', s4 = '금요일입니다.'
#print(fs1, s2, s3, s4)

#a = int(input('Please enter integer you wnat: '))
#b = int(input('Please enter integer you want: '))
#def A(a,b):
    #return a+b, a-b

#print(A(a,b))

#c = int(input('Please enter integer you want: '))
#d = int(input('Please enter integer you want: '))

#list2 = [a, b, c, d]
#def B (list2):
    #C = list2[0] + list2[1]
    #return C

#def D(list2):
    #E = list2[-1]+ list2[-2]
    #return E

#print(B(list2))
#print(D(list2))

#import math as m
#pi = m.pi
#from math import pi
#a = pi*(10**7)%10
#print (int(a))
#pi = str(pi)
#print(pi[8])

def fib(n):
    array1 = []
    a, b = 0, 1
    while a < n:
        array1.append(a)
        a, b = b, a+b
    return array1

print(fib(100))

m = int(input('Please enter integer: '))
def fib(m):
    array2 = [1,1]
    k = 2
    if m == 1:
        array2 = [1]
        return array2
    elif m == 2:
        array2 = [1, 1]
        return array2
    elif m > 3:    
        while  k < m:
            c = array2[-1] + array2[-2]
            array2.append(c)
            k += 1
        return array2
print(fib(m))

