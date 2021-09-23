# 외벽 점검
from itertools import permutations
def func(r,result,n,weak,dist,cnt):
    answer = -1
    n -= r[3]

    result.remove(r)




def solution(n, weak, dist):

    sets = list(map(list,permutations(weak, 2))) #[start,end]
    results = []
    num = len(weak)

    #각 지점간의 거리와 점 개수
    for s in sets:
        cnt = 0
        if s[0] > s[1]:
            d = (n-s[0])+s[1]
            cnt+=(num-weak.index(s[0]) + weak.index(s[1])+1)
        elif s[0] < s[1]:
            d = s[1]-s[0]
            cnt = weak.index(s[1])-weak.index(s[0])+1
        results.append([s[0], s[1], d,cnt])

    #완탐?
    max_d = max(dist)
    result = [r for r in results if r[2]<= max_d]
    result.sort(key=lambda x: (x[2], x[3]), reverse=True)

    answer = -1
    for r in result :
        if r[3] == n :
            return 1
        else :
            sum = func(r,result,n,weak,dist,0)
            if -1 < sum and sum < answer :
                answer = sum

    return answer


