## 성균관대학교 프로그래밍 A번
# 내 뒤에 나와 다른 수

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def solution(n, arr):
    answer = []
    for i in range(n) :
        if i == n-1:
            answer.append(-1)
            break
        res_arr = arr[i+1:]
        small = min(res_arr)
        if arr[i] == small:
            # sort_arr = list(set(sorted(res_arr)))
            sort_arr = list(set(res_arr))
            sort_arr.remove(small)
            
            if sort_arr == []:
                answer.append(-1)
                continue
            else:
                small = min(sort_arr)

        idx = res_arr.index(small)
        answer.append(i+idx+2)

    return list(map(str,answer))

print(*solution(n,arr))
