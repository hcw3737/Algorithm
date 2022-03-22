# DP # 소형기관차

import sys
input = sys.stdin.readline

n = int(input())
train = [0] + list(map(int, input().split()))
m = int(input())

dp = [[0]*(n+1) for _ in range(4)]

for i in range(1,4):
    for j in range(i*m, n+1):
        dp[i][j] = max(dp[i-1][j-m]+sum(train[j-m+1:j+1]),dp[i][j-1])

print(dp[3][-1])
