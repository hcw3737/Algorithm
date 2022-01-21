# BFS/DFS 문제

from collections import deque
def solution(n, computers):
    visited = [[0]*n for _ in range(n)]

    def bfs():
        count = 0
        answer = []

        for i in range(n):
            for j in range(n):
                if computers[i][j]==1 and visited[i][j]==0:

                    # count += 1
                    answer.append([i,j])

                    queue = deque()
                    queue.append([i,j])

                    while queue :
                        x, y = queue.popleft()
                        visited[x][y] = 1
                        visited[y][x] = 1

                        if sum(computers[j]) == 1:
                            count += 1
                            break

                        for idx, k in enumerate(computers[y]):
                            if k==1 and idx == y:
                                visited[y][idx] = 1
                                continue
                            if k==1 and visited[y][idx] == 0:
                                queue.append([y, idx])
                            else :
                                visited[y][idx] = 1
                                visited[idx][y] = 1

        return len(answer) #count

    return bfs()
  
  # 다른 사람 풀이
  def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer
