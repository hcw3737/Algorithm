# 이친수

N = int(input())

d = [0]*(N+1)
d[0] = 0
d[1] = 1
for i in range(2,N+1):
    d[i] = d[i-2] + d[i-1]
    
print(d[N])
