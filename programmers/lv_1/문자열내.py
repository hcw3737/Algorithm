#문자열 s
#p,y개수 같으면 true / 다르면 false
#pyahen 하나도 없으면 true
#대소문자 구분X

s = str(input())
def solution(s):
    s = s.lower()
    ss = list(map(str,s))
    l = [0]*2
    for a in ss :
        if a == 'p' :
            l[0] += 1
        elif a == 'y' :
            l[1] += 1
    if l[0]==0 and l[1]==0 :
        answer = True
    elif l[0]==l[1] :
        answer = True
    elif l[0]!=l[1] :
        answer = False
    return answer


## 다른 사람 풀이

def numss(s) :
    s = s.lower()
    return s.count('p') == s.count('y')
    #맞으면 true, 다르면 false

print(numss(s))
