# a,b sort하고 차례로 더함

def solution(a, b):
    answer = 0
    k = [a,b]
    k.sort()
    i = k[0]
    while i <= k[1] :
        if i == k[1] :
            answer += k[1]
            break
        else :
            answer += i
            i += 1
    return answer

print(solution(5,3))

#다른 사람 풀이

def adder(a,b) :
    if a>b :
        a,b = b,a
    return sum(range(a,b+1))    #그래야 a부터 b까지의 합

