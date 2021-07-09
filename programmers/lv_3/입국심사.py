# 입국심사

def solution(n, times):
    answer = 0
    n_time = len(times)
    line = [[0] for _ in range(n_time)]

    for i in range(n) :
        if i == 0 :
            line[0]
        elif i != n-1 :
            last_time = []
            for j in range(n_time):
                last_time.append(line[j][-1])
            min_t = min(last_time)
            l = last_time.index(min_t)
            line[l].append(min_t + times[l])
        elif i == n-1 :
            last_time = []
            for j in range(n_time):
                last_time.append(line[j][-1] + times[j])
            min_t = min(last_time)
            l = last_time.index(min_t)
            answer = min_t

    return answer

# hidden case 실패..


########################################################################

# 풀이

# binary search 이분 탐색법
# binary search를 위해서는 먼저 sorting이 필요하다(단점)
def binary_search(arr, val):
    first, last = 0, len(arr)
    while first <= last:
        mid = (first + last)//2
        if arr[mid] == val : return mid
        if arr[mid] > val : last = mid-1
        else : first = mid+1

    return -1


# def solution(n, times):
#     answer = 0
#     # line = dict()
#     # for t in times:
#     #     line[t] = 0
#     # line.items()
#     return

def solution(n, times):
    #binary search를 위한 sorting
    times.sort()

    #기다리는 사람 1명, 심사관 1명일 때 최소시간
    min_time = 1

    #기다리는 사람 모두 심사시간이 가장 긴 심사관에게 갈 때 최대시간
    max_time = times[len(times)-1]*n

    aswer = max_time

    while(min_time <= max_time) :
        mid_time = int((min_time + max_time)/2)

        sum = 0
        # mid_time 일때, 몇 명 검사할 수 있는지 체크
        for i in range(len(times)):
            sum += int(mid_time/times[i])

        # n명 보다 더 많은 사람을 검사할 수 있을 때 최대시간 감소
        if(sum >= n):
            if(answer > mid_time):
                answer = mid_time
            max_time = mid_time-1

        # n명보다 더 적은 사람을 검사할 수 있을 때 최소시간 증가
        else:
            min_time = mid_time+1

    return answer
