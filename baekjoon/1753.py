# 최단 경로
# 다익스트라 알고리즘

import sys
input = sys.stdin.readline  # 시간 초과 해결

v, e = map(int, input().split()) # 정점, 간선 개수
start = int(input())  # 시작 정점

graph = [[] for _ in range(v+1)]  # 0번째 제회하고 v개여야해서
distance = [1e9]*(v+1)

for _ in range(e):
    u, a, w = map(int, input().split())
    graph[u].append([a,w])  # 시작, 도착, 가중치

import heapq
def dijk(start):
    q = []
    heapq.heappush(q,(0,start)) # 자기 자신한테 가는 건, 가중치 0
    distance[start] = 0  # 거리(횟수)도 0
    
    while q:
        dist, now = heapq.heappop(q)  # 가중치, 현재 지점
        
        if distance[now] < dist :  # 이미 처리된 경우, 무시
            continue
        
        for i in graph[now]:
            cost = dist+i[1]  #i[1] : 연결된 노드 중 하나로 가는 데 필요한 가중치
            # i[0] : 연결된 노드 번호로, 해당 노드까지 가는데 필요한 가중치 합계가 최소인 경우
            if cost < distance[i[0]] :  
                distance[i[0]] = cost   # 갱신
                heapq.heappush(q,(cost,i[0]))  # heapq에 push

dijk(start)

for i in range(v):
    if distance[i+1]==1e9:  # 도착 불가한 경우
        print('INF')
    else :
        print(distance[i+1])
