# 1로 만들기

N = int(input())

# 1일때는 더이상 연산이 필요 없기 때문에 0으로 초기화 유지
d = [0] * (10**6+1)

# 보텀업 방식
for i in range(2, N+1):
    # 현재 수에서 1을 빼는 경우
    d[i] = d[i-1] +1
    # 현재 수가 2로 나누어 떨어지는 경우
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    # 현재 수가 3으로 나누어 떨어지는 경우
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)

print(d[N])
