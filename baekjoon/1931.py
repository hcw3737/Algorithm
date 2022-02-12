n = int(input())

meeting = []
for _ in range(n):
    meeting.append(list(map(int, input().split())))
    
meeting.sort(key = lambda x:(x[1], x[0])) # 제일 먼저 끝나는 회의부터 정렬

last = 0
cnt = 0

for i, j in meeting:
    if i>=last:  # last 회의 이후일 경우, 정렬해놓았기 때문에 다른 코드는 필요하지 않다.
        cnt+=1
        last=j

print(cnt)
