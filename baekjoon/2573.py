# 백준 2573. 빙산

from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

day = 0

def melt(graph, i, j):
    cnt = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 > nx or nx >= N or 0 > ny or ny >= M :
            continue
        elif graph[nx][ny] == 0:
            cnt += 1

    if graph[i][j] - cnt < 0:
        result = 0
    else :
        result = graph[i][j] - cnt

    return result

def melt_count(graph): # 덩어리 개수 세기
    count = 0

    for i in range(N) :
        for j in range(M) :
            if graph[i][j] <= 0 :
                continue
            else :
                queue = deque([])
                queue.append([i,j])

                while queue :
                    x, y = queue.popleft()
                    for k in range(4) :
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] > 0:
                            graph[nx][ny] = -1
                            queue.append([nx,ny])
                count += 1

    # 모두 0 인 경우, return 0
    # 2개 이상 분리된 경우, return 덩어리수
    if count == 0 :
        return 0
    elif count == 1 :
        return 1
    elif count > 1:
        return count

    return count

def solution(board, day):
    day += 1
    board1 = [[0]*M for _ in range(N)]

    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 0:
                continue
            else :
                board1[i][j] = melt(board,i,j)
                # print(i,j,board[i][j], board1[i][j])

    board2 = board1.copy()
    cnt = melt_count(board1)

    if cnt > 1:
        return day
    elif cnt == 0 :
        return 0
    elif cnt == 1 :
        solution(board1)
        return board1

    return 0 #board1



# 다른 사람 풀이

from collections import deque

n, m = map(int, input().split())
board = [[map(int, input().split())] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()
day = 0
check = False

def bfs(a,b):
    queue.append([a,b])
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m :
                if board[nx][ny] != 0 and visited[nx][ny] == False :
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                elif board[nx][ny] == 0:
                    count[x][y] += 1
    return 1

# 빙산이 분리될때까지 돈다
while True:
    visited = [[False]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))

    # 빙산을 깎음
    for i in range(n):
        for j in range(m):
            board[i][j] -= count[i][j]
            if board[i][j] < 0:
                board[i][j] = 0

    if len(result) == 0:    # 빙산이 다 0
        break
    if len(result) >= 2:
        check = True
        break
    day += 1

if check:
    print(day)
else:
    print(0)
