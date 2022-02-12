# DP로 해결? 시간 초과...

 n = int(input())

def dfs(n):
    dp = []
    queue = [[3],[5]]

    while queue:
        m = queue.pop(0)
        l = m.copy()
        if sum(m) == n:
            dp.append(len(m))
        if sum(m)+3<=n :
            m.append(3)
            queue.append(m)
            dp.append(sum(m))
        if sum(l)+5<=n:
            l.append(5)
            queue.append(l)
            dp.append(sum(l))

    if len(dp) != 0:
        return min(dp)
    else :
        return -1

    return -1

print(dfs(n))


# 다른 풀이

sugar = int(input())
bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)
