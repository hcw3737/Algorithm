#n은 진법, t는 판수, m 참가인원, p 튜브 순서

def solution(n, t, m, p):
    answer = ''
    str_list = []
    if n <= 10 :
        for a in range(t*m) :
            res = []
            if a == 0 : res.append(0)
            else :
                while a!=0:
                    res.append(a%n)
                    a=a//n
            str_list += list(reversed(res))
    elif n > 10 :
        for a in range(t*m) :
            res = []
            if a == 0 : res.append(0)
            else :
                while a!=0:
                    if a%n >= 10:
                        res.append(chr(a%n+55))
                    else :
                        res.append(a%n)
                    a=a//n
            str_list += list(reversed(res))
    for a in range(len(str_list[:t*m])) :
        if a%m == (p-1) :
            answer += str(str_list[a])
    return answer


# ord('A') #65
n = 16
t = 16
m = 2
p =2


n = 2
t = 4
m = 2
p = 1
