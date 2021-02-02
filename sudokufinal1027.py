sudoku = [                                  #수도쿠 예시(1행1열, 9행9열만 완성하면 끝나는 수도쿠)
    [0,7,4,1,9,6,8,2,5],
    [5,2,1,4,7,8,9,3,6],
    [6,9,8,2,5,3,7,1,4],
    [8,1,9,6,4,7,2,5,3],
    [4,3,2,5,8,9,6,7,1],
    [7,6,5,3,1,2,4,9,8],
    [1,4,7,8,2,5,3,6,9],
    [9,5,6,7,3,4,1,8,2],
    [2,8,3,9,6,1,5,4,0],
]

def check1(array):                                  #check1은 각 행의 1~10의 숫자가 한번씩 들어가는지 검사해준다.
    resultrow = True                                #if문을 통과하지 않게되면 True값을 return한다.                     
    for row in range(9):                            #for문을 돌면서 row는 각행을 가르킨다.    
        check_row = []                              #check_row는 각 행의 요소를 받는 list이다. 
        for a in range(9):                          #for문을 돌면서 a는 각행의 1~9까지 요소들을 가르킨다.
            check_row.append(array[row][a])         #array(sudoku)의 row행 a열 요소들을 check_row로 받는다.
        for n in range(1,10):                       
            if check_row.count(n) != 1:             # 각행의 요소들이 1~10까지 숫자들이 딱 한개씩만 들어가는지 검사한다.
                resultrow = False
    return resultrow                                #1~10까지 각 요소들이 한번씩들어가면 True, 아니면 False

def check2(array):                                  #check2는 각열의 1~10의 숫자가 한번씩 들어가는지 검사해준다.    
    resultcolumn = True                             #code는 check1과 매우 유사하다.
    for column in range(9):
        check_column = []
        for a in range(9):
            check_column.append(array[a][column]) #check_column은 array의 각 열의 요소들을 받는다.  
        for n in range(1,10):
            if check_column.count(n) != 1:
                resultcolumn = False
    return resultcolumn


def check3(array):                                      #3*3box안에 1~9까지 숫자가 하나씩들어가는지 검사하는 함수이다. 
    resultbox = True
    checkbox1 = [] 
    checkbox2 = []
    checkbox3 = []
    checkbox4 = [] 
    checkbox5 = []
    checkbox6 = []
    checkbox7 = []
    checkbox8 = []
    checkbox9 = []
    for i in range(9):                                #9*9수도쿠를 9개의 3*3box를 구분해준다.
        if i <= 2:                                    #1,2,3행일때를 가리킨다.  
            for j in range(9):
                if j <= 2:                              
                    checkbox1.append(array[i][j])     #1,2,3행 1,2,3열 요소들을 checkbox1이라는 list로 모은다.  
                elif 2 < j < 6 :
                    checkbox2.append(array[i][j])     #1,2,3행 4,5,6열 요소들을 checkbox2라는 list로 모은다.
                elif  5 < j < 9 :
                    checkbox3.append(array[i][j])
        elif 2 < i < 6:                               # 아래 방법도 위와 같이 행과 열을 구분해서 checkbox'n'으로 모은다.   
            for j in range(9):
                if j <= 2:
                    checkbox4.append(array[i][j])
                elif 2 < j < 6 :
                    checkbox5.append(array[i][j])
                elif  5 < j < 9 :
                    checkbox6.append(array[i][j])
        elif 5 < i < 9:
            for j in range(9):
                if j <= 2:
                    checkbox7.append(array[i][j])
                elif 2 < j < 6 :
                    checkbox8.append(array[i][j])
                elif  5 < j < 9 :
                    checkbox9.append(array[i][j])
    for n in range(1,10):                               #n을 1~9까지 돌리면서 각 checkbox의 요소들의 성분이 1~9까지 숫자가 한번씩 들어기는지 검사해준다.
        if checkbox1.count(n) != 1:                #만약 1~9까지 숫자가 한번씩들어가지 않으면 False를 return한다.
            resultbox = False
        elif checkbox2.count(n) != 1:
            resultbox = False
        elif checkbox3.count(n) != 1:
            resultbox = False
        elif checkbox4.count(n) != 1:
            resultbox = False
        elif checkbox5.count(n) != 1:
            resultbox = False        
        elif checkbox6.count(n) != 1:
            resultbox = False
        elif checkbox7.count(n) != 1:
            resultbox = False
        elif checkbox8.count(n) != 1:
            resultbox = False
        elif checkbox9.count(n) != 1:
            resultbox = False
    return resultbox          

while check2(sudoku) == False or check2(sudoku) == False or check3(sudoku) == False: # check123가 다 False일 동안은 계속 반복한다.
    print(sudoku)                                            #바뀐 sudoku를 출력하고       
    #print(check1(sudoku),check2(sudoku),check3(sudoku))     # 바꾸고 싶은 행과열, 그리고 요소들을 input으로 받는다.
    r = int(input('Please enter row you want to change: ' ))
    c = int(input('Please enter collum you want to chage'))
    i = int(input('Please enter integer'))
    sudoku[r-1][c-1] = i                                    #sudoku의 r행c열의 요소를 i로 바꾼다.
if check1(sudoku) == True and check2(sudoku) == True and check3(sudoku) == True: #만약 check123가 다 True이면 게임을 끝낸다.
    print('Congratulation! you win!')