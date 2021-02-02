sudoku = [
    [9,8,0,0,0,6,3,0,0],
    [0,0,0,3,0,7,5,2,0],
    [0,2,3,0,5,0,4,0,9],
    [1,6,2,0,0,4,9,0,5],
    [8,0,0,6,0,5,0,0,3],
    [5,0,4,2,0,0,6,7,1],
    [3,0,1,0,6,0,8,9,0],
    [0,4,9,8,0,3,0,0,0],
    [0,0,8,9,0,0,0,3,2],
]
def box(array=sudoku):                              #3*3box를 9개만드는 함수
    box = [[],[],[],[],[],[],[],[],[]]              #box라는 list의 box'n'을 모아줍니다.
    for i in range(9):                              #i는 sudoku에서 행을 의미합니다.                
        if i <= 2:                                  #123행을 처리하는 if문입니다.       
            for j in range(9):                      
                if j <= 2:                          
                    box[0].append(array[i][j])      #1행1,2,3열,2행1,2,3열,3행1,2,3열의 요소들을 box의 행으로 모읍니다.    
                elif 2 < j < 6 :                    #아래 방법은 위와 똑같은 방법으로 box list의 각 행으로 sudokubox의 요소들을 모읍니다.
                    box[1].append(array[i][j])
                elif  5 < j < 9 :
                    box[2].append(array[i][j])
        elif 2 < i < 6:
            for j in range(9):
                if j <= 2:
                    box[3].append(array[i][j])
                elif 2 < j < 6 :
                    box[4].append(array[i][j])
                elif  5 < j < 9 :
                    box[5].append(array[i][j])
        elif 5 < i < 9:
            for j in range(9):
                if j <= 2:
                    box[6].append(array[i][j])
                elif 2 < j < 6 :
                    box[7].append(array[i][j])
                elif  5 < j < 9 :
                    box[8].append(array[i][j])
    return box

def checkbox(r,c):                          # sudoku의 r행c열의 요소가 어떤 sudoku box에 해당하는지 구분해주는 함수입니다. 
    boxx = box(sudoku)
    if r <= 2:                              #1,2,3행 중                                     
        if c <= 2:                          #1,2,3열 의 요소이면 sudoku box1을
            return boxx[0]                  #return값을 boxx의 리스트의 한 행으로 지정했는데, 나중에 검사하는 function에서 효과를 봅니다.
        elif 2 < c <6:                      #아래 방법은 위와 같은 방법입니다.
            return boxx[1]
        else:
            return boxx[2]
    if 2 < r < 6:
        if c <= 2:
            return boxx[3]
        elif 2 < c <6:
            return boxx[4]
        else:
            return boxx[5]
    elif 5 < r < 9 :
        if c <= 2:
            return boxx[6]
        elif 2 < c <6:
            return boxx[7]
        elif 5 < c < 9:
            return boxx[8]

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
                    elif n in checkbox(i,j):            #1~9의 숫자가 해당 box의 있을 때 pass합니다.
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