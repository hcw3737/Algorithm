
import sys
from collections import deque

M, N, K = map(int, input().split(' '))
graph = [[0]*N for _ in range(M)]
for _ in range(K):
    a,b,c,d = map(int, input().split(' '))
    for i in range(a, c):
        for j in range(b, d):
            graph[j][i] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(y,x):
    que = deque()
    que.append([x,y])
    graph[x][y]
