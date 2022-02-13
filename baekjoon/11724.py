# 11724
# BFS - 연결 요소의 개수

## Solution.1

from collections import deque
import sys
input = sys.stdin.readline  # 시간 초과 해결

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(x,y):
    queue = deque()
    queue.append([x,y])

    while queue:
        nx, ny = queue.popleft()
        if graph[nx] != []: 
            for i in graph[nx]:
                queue.append([nx,i])
                graph[nx].remove(i)
        if graph[ny] != []: 
            for j in graph[ny]:
                queue.append([ny,j])
                graph[ny].remove(j)
    return graph

cnt = 0
for i in range(n):
    if graph[i+1] != []:
        graph = bfs(i+1,graph[i+1][0])
        cnt+=1

print(cnt)


## Solution.2

from collections import deque
import sys
input = sys.stdin.readline  # 없으면 시간 초과 발생

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if visited[i] == False:  # 미방문 노드일 경우
                queue.append(i)
                visited[i] = True

cnt = 0
for i in range(1,n+1):
    if visited[i] == False:  # 미방문 노드일 경우
        bfs(graph, i, visited)
        cnt+=1

print(cnt)
