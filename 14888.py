from itertools import permutations

N = int(input())
m, n = map(int, input().split(' '))
operator = list(map(int, input().split(' ')))
# +, -, *, /
oper_list = []
for idx, o in enumerate(operator) :
    for _ in range(o):
        oper_list.append(idx)


def rule(a,b,oper):
    answer = 0
    if oper == 0:
        answer = a+b
    elif oper == 1:
        answer = a-b
    elif oper == 2:
        answer = a*b
    elif oper == 3:
        if a < 0:
            answer = -(abs(a)//b)
        elif a==0:
            answer = 0
        else :
            answer = a//b
    return answer

# 경우의 수 조합
set(permutations(oper_list, len(oper_list)))
