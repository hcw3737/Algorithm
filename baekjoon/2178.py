# BFS

from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
  board.append(list(map(int, input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    start = [0,0]
    queue = deque()
    queue.append(start)

    while queue :  # queue가 비어있을 때까지 실행
        x, y = queue.popleft()

        for i in range(4):  # 4방향 순서대로 접근
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m: # 배열 범위 이탈한 경우 - 무시
                continue
            elif nx==n-1 and ny==m-1: # 마지막 셀 도착한 경우 - 종료
                return board[x][y]+1
            elif board[nx][ny] == 1: # 길이 있는 경우 - 이전 경로+1, queue에 삽입
                board[nx][ny] = board[x][y]+1
                queue.append([nx,ny])

    return board[n-1][m-1]

print(bfs())
