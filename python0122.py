#a = 0 
#while a <= 3:
#   print(' |  |  ')
#   print('-----')
#    a = a + 1

for n in range(3):
    if n%3 == 0:
        print ('가위')
    elif n%3 == 1:
        print ('바위')
    else:
        print ('보')

for i in range(5):
    if i%2 == 0: #even number, even row, odd columun
        for j in range(1,6):
            #print ('i, j', i, j)
            if j%2 == 1 : #odd number
                print (' ', end='')
                if j == 5: 
                    print(' ')
                else:
                    print(' ')
            else:
                print('|', end='')
    else:
        print('-----')

myUniquelList = []

def addlist(var):
    global myUniquelList
    if var in myUniquelList:  
        return False
    else:
        myUniquelList.append(var)
        result = True
        return result
print(myUniquelList, addlist('a'))


for i in range(5):
    if i%3 == 0:
        if i%5 == 0:
            print(i,'셋다섯')
        else:
            print(i,'셋')
    elif i%5 == 0:
        print(i,'다섯')
    else:
        print(i)
i=9
def function(arg=i):
    print(arg)

function(3)

def ask(prompt, tries = 2, reminder='Plese rspond properly'):
    while True:
        ans = input(prompt+' ')
        if ans in ('y', 'yes', 'yeah'):
            print('You have answered yes')
            return True
        elif ans in ('n','no','nah'):
            print('you have answered no')
            return False
        print(reminder)
        tries = tries -1
        if tries == 0:
            break
        
        #return
ask('Introduce your answer')

#def function(var, *var1, **var2): #*붙으면 튜플로 불러올수 있음