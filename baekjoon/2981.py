from  sys import stdin
input = stdin.readline

#검문 시간 오래걸려서 수학게임..
# N,n,P,p = map(int, input().split())
N = int(input())
num = []
for _ in range(N):
    a = int(input())
    num.append(a)

answer = []
#최대값까지 모두 적용해보기(greedy..)
max_num = max(num)
for i in range(2,max_num+1):
    res = []
    for idx, a in enumerate(num):
        r = a%i
        if idx == 0 :
            res.append(r)
        elif res[0] != r:
            break
        elif idx == len(num) and res[0] == r:
            answer.append(i)
    # if len(set(res)) == 1:
    #     answer.append(i)

answer = list(map(str, answer))
result = " ".join(answer)
print(result)


#개수가 10만개면, 100*10만 = 1000만번 수행


유클리드호제법

