
# https://www.acmicpc.net/problem/1743
# DFSBFS  # 음식물피하기

from collections import deque
import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
graph = [[0]*m for _ in range(n)]

for _ in range(k):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    graph[i][j] = 2

    sum = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                q.append([nx,ny])
                graph[nx][ny] = 2  # 방문 처리
                sum+=1

    return sum

max = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            size = bfs(i,j)
            if max <= size:
                max = size

print(max)
