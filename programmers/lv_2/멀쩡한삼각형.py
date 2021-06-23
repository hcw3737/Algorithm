# 멀쩡한 사각형
def solution(w, h):
    if w == h: return (w * h - w)

    def gcd(a, b):          #최대공약수
        if b == 0: return a
        return gcd(b, a % b)

    if w > h:
        l = w
        s = h
    else:
        l = h
        s = w

    g = gcd(l, s)
    return w * h - (w + h - g)

if type(i) == int : #이런식으로 x가 정수일때는 찾을 수 있다. 하지만 비효율적


#####################################################################################
  
import math
def solution(w,h) :
    return w*h - (w+h-math.gcd(w,h))        #최대공약수를 이용해 x가 정수일 때를 찾아냄.

print(solution(8,12))
