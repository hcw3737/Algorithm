# DFS 유기농배추

t = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(board,x,y):
    if board[x][y] != 1:
        return
    if board[x][y] == 1:
        board[x][y] = 2
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0>nx or nx>=len(board) or 0>ny or ny>=len(board[0]):
                continue
            else:
                dfs(board, nx, ny)
    return board

def solution(board,n,m):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cnt+=1
                board = dfs(board, i, j)
    return cnt

for _ in range(t):
    n,m,c = map(int, input().split()) # 가로, 세로, 배추 개수
    board = [[0]*m for _ in range(n)]

    for _ in range(c):
        i, j = map(int, input().split()) # 열, 행번호
        board[j][i] = 1

    print(solution(board,m,n))
