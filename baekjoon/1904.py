# 01타일

N = int(input())

d = [0] * (1000001)

# 피보나치 수열
d[1]=1
d[2]=2
for i in range(3,N+1):
    d[i] = (d[i-2]+d[i-1])%15746

print(d[N])
