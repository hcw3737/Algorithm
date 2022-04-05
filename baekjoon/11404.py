
# https://www.acmicpc.net/problem/11404
# 플로이드-와샬  # 플로이드


n = int(input())
m = int(input())

graph = [[1e9]*n for _ in range(n)]

for _ in range(m):
    i, j, c = map(int, input().split())
    graph[i-1][j-1] = min(graph[i-1][j-1], c)

for k in range(n):  # 경유지
    graph[k][k] = 0
    for  i in range(n):   # 출발지
        for j in range(n):    # 목적지
            # 경유지 포함X, 포함 비교
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for row in graph:
    for c in range(n):
        if row[c] == 1e9:
            row[c] = 0
        print(row[c], end=" ")
    print() # 다음 줄 tab
