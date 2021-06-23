# 가운데 글자
# import math

ss = list(map(str,input()))

def solution(s):
    ll = int(len(s))     #2로 나눴을때, 5글자일 경우 2.5-> 3을 가져옴(인덱스 2)
    if ll%2 == 0 :       #짝수면, 4인경우 2,3 --> 1,2
        i = (ll//2)-1
        j = (ll//2)
        answer = str(s[i])+str(s[j])
    else :               #홀수인 경우
        i = round(ll//2) #원래 math.ceil() - 1
        answer = str(s[i])
    return answer

print(solution(ss))

#math.ceil(2.5)


#다른 사람 풀이
def string_middle(s) :
    return s[(len(s)-1)//2 : len(s)//2+1]
            #홀수면 2:3 , 짝수면 1:3 이런식으로 나타날테니까 (5일경우)
