import numpy as np
sudoku =np.array([
    [9,8,0,0,0,6,3,0,0],
    [0,0,0,3,0,7,5,2,0],
    [0,2,3,0,5,0,4,0,9],
    [1,6,2,0,0,4,9,0,5],
    [8,0,0,6,0,5,0,0,3],
    [5,0,4,2,0,0,6,7,1],
    [3,0,1,0,6,0,8,9,0],
    [0,4,9,8,0,3,0,0,0],
    [0,0,8,9,0,0,0,3,2],
])
def checkbox(i,j,array):
    i_start = 3*(i//3)  #i를 3으로 나눈 나머지 곱하기 3
    j_start = 3*(j//3)  #j를 3으로 나눈 나머지 곱하기 3
    boxarray =[]        
    for k in range(i_start,i_start+3):
        for l in range(j_start,j_start+3):
            boxarray.append(array[k][l])
    return boxarray

def check(array):                                       #sudoku의 빈칸에 어떤 숫자가 넣어야되는지 계산하는 함수입니다.    
    coulmn = [[],[],[],[],[],[],[],[],[]]               #sudoku의 각 열을 하나의 행렬의 각 요소로 받게 했습니다.
    for c1 in range(9):                                 # c1은 행입니다.            
        for c2 in range(9):                             # c2는 열입니다.
            coulmn[c1].append(array[c2][c1])            # append할때 행과 열을 바꾸었기에 colmn은 array의 transposed matrix가 됩니다.
    
    for i in range(9):                                  #각 행 각열 을 검사하는 for문입니다.
        for j in range(9):
            possible = []                               #possible list는 빈칸에 들어갈 수 있는 숫자들을 받습니다.
            if array[i][j] != 0:                        #0(빈칸)이 아니면 검사하지 않습니다. 
                pass
            elif array[i][j] == 0:                      #0(빈칸)이면 검사합니다.
                for n in range(1,10):
                    if n in array[i]:                   #1~9의 숫자가 해당 열에 있을 때 pass합니다.    
                        pass
                    elif n in coulmn[j]:                #1~9의 숫자가 해당 열에 있을 때 pass합니다.
                        pass
                    elif n in checkbox(i,j,array):            #1~9의 숫자가 해당 box의 있을 때 pass합니다.
                        pass
                    else:
                        possible.append(n)              #n이  행과 열과 box의 없을때 possible list에 모읍니다.
            if len(possible) == 1:                      #만약 possible에 들어 있는 n이 하나일 경우 그 n을 sudoku빈칸에 넣습니다.
                array[i][j] = int(possible[0])
                
    return array
def lastcheck(array=sudoku):                        #check함수를 가동 했을때 0(빈칸)이 존재하면 False를 return하는 함수입니다.
    last = check(array)                             #check함수를 거쳐나온 array를 last로 받습니다.
    result = True
    for i in range(9):                              #last(수정한 array)의 각 행의 0의 갯수가 0개가 아니면 False을 retrun합니다.
        if last[i].count(0) != 0:
            result = False
    return result
while lastcheck(sudoku) == False:                   #lastcheck가 False 경우 계속 check를 가동해주는 함수입니다.
    check(sudoku)
if lastcheck(sudoku) == True:                       #lastcheck가 True일 경우 즉 0(빈칸)이 없을 경우 게임을 프로그램을 종료합니다.
    print(check(sudoku))    