# 1~m 까지 숫자 중 n개의  수
# greedy?

import math
from  sys import stdin
input = stdin.readline

def lotto(n,m):
    answer = []
    # 이전 값 보다 2배보다 크거나 같은 값이어야함
    # 최소 최대
    min = [1]
    max = [m]

    for i in range(n-1):
        x = min[-1]*2
        min.append(x)
    for j in range(n-1):
        y = math.trunc(max[-1]/2)
        max.append(y)


    return answer

T = int(input())
N = []
M = []

for _ in range(T):
    n,m = list(map(int, input().split()))
    N.append(n)
    M.append(m)

for i in range(T):
    result = lotto(N[i],M[i])
    print(result)

