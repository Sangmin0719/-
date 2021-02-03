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

def check3(array):
    result = True                                      #3*3box안에 1~9까지 숫자가 하나씩들어가는지 검사하는 함수이다.  
    for i in range(0,7,3):
        for j in range(0,7,3):
            box=[]
            for k in range(i,i+3):
                for l in range(j,j+3):
                    box.append(array[k][l])
            for n in range(1,10):
                if box.count(n) != 1:
                    result = False
    return result
                        
                            


while check2(sudoku) == False or check2(sudoku) == False or check3(sudoku) == False: # check123가 다 False일 동안은 계속 반복한다.
    print(sudoku)                                            #바뀐 sudoku를 출력하고       
    #print(check1(sudoku),check2(sudoku),check3(sudoku))     # 바꾸고 싶은 행과열, 그리고 요소들을 input으로 받는다.
    r = int(input('Please enter row you want to change: ' ))
    c = int(input('Please enter collum you want to chage'))
    i = int(input('Please enter integer'))
    sudoku[r-1][c-1] = i                                    #sudoku의 r행c열의 요소를 i로 바꾼다.
if check1(sudoku) == True and check2(sudoku) == True and check3(sudoku) == True: #만약 check123가 다 True이면 게임을 끝낸다.
    print('Congratulation! you win!')