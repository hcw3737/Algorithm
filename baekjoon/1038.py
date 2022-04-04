# https://www.acmicpc.net/problem/1038
# back tracking # 감소하는 수

from itertools import combinations

n = int(input())

num = [] 
for i in range(1, 11): 
    for comb in combinations(range(0, 10), i):  
        comb = list(comb)
        comb.sort(reverse=True) 
        num.append(int("".join(map(str, comb))))

num.sort()

try :
    print(num[n])
except :
    print(-1)
