import math

def prime_num(p):
    if p==0 or p==1:
        return False
    else :
        for i in range(2, int(math.sqrt(p))+1):
            if p%i==0:
                return False
        return True

def solution(n, k):
    answer = []

    result = ''
    #n진법
    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)
    rev_result = result[::-1]

    prime = list(map(str, rev_result.split('0')))

    #소수
    for p in prime :
        if p != '' and prime_num(int(p)) :
            answer.append(p)

    return len(answer)
