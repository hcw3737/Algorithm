#삼각 달팽이
def solution(n):
    answer = []
    board = [[0]*n for _ in range(n)]
    x,y = -1,0
    num = 1
    for i in range(n) :
        for j in range(i,n) :
            if i%3 == 0 :
                x+=1
            elif i%3 == 1:
                y+=1
            elif i%3 == 2:
                x-=1
                y-=1

            board[x][y] = num
            num+=1

    for i in board :
        for j in i :
            if j!=0 :
                answer.append(j)

    return answer

n = 6
print(solution(n))
