# 약수 구하기 + 서로 다른 소수 곱하기

import math

def is_prime(x):
    for i in range(2, int(math.sprt(x))+1):
        if x%i==0:
            return False
    return True

def solution(n):
    num = []
    for i in range(1, n+1):
        if n%i==0:
            a=n//i
            b=n//a
            if a<=b : break
            else :
                num.append([b,a])

    for x, y in num :
        if is_prime(x)==True and is_prime(y)==True:
            return [x,y]
