# 이분탐색 - 징검다리

# 이전에 건너 수보다 최소 1보다 커져야한다.
# 건너는 횟수 최대화
# 1+2+....+k-1+k = N 이 되면, 횟수를 최대화시킬 수 있다.
# 만약 +k를 했을때, N보다 크면, k-1값과 k을 함께 조정하면 된다.
# ex) 1+2+3+4>9 이므로, 1+2+6=9 이런식 만들어준다.

t = int(input())

def k_func(n, k):
    num = k*(k+1)//2
    if num <= n:    #마지막 징검다리보다 작거나 같으면
        return True
    else:
        return False

def binary_search(n): # k값 찾기 위해
    # 1+2+....+k-1+k = k*(k+1)/2
    ans = 0
    left, right = 1, 1e9

    while left<=right :
        mid = (left+right)//2
        print(mid)
        if k_func(n, mid)==False:
            right = mid-1
        else:
            ans = mid
            left = mid+1

    return int(ans)

for _ in range(t):
    n = int(input())
    print(binary_search(n))
