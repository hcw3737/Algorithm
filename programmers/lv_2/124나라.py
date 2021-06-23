#124나라의 숫자
import itertools
def solution(n):
    num_list = []
    t = 0
    i = 1
    while (True) :
        t_origin = t
        t+=3**i
        if t >= n:
            num_list += list(map(int,map("".join,(itertools.product(['1','2','4'],repeat = i)))))
            answer = str(num_list[n-t_origin-1])
            # answer = i
            break
        else :
            i+=1
    return i,answer

n=49
print(solution(n))
#시간초과....

import itertools
def solution(n):
    num_list = []
    t = 0
    i = 1
    while (True) :
        t+=3**i
        if t >= n:
            while 3**i>=3:
                if i==1 :
                    num_list.append(str(n//(3 ** i)))
                    num_list.append(str(n%(3 ** i)))
                    break
                num_list.append(str(n//(3**i)))
                n = n%(3**i)
                i-=1
            # answer = i
            break
        else :
            i+=1
    for i in range(len(num_list)):
        if num_list[i] == 3:
            num_list[i] = 4

    answer = "".join(num_list[1:])

    return answer

n=49
print(solution(n))


def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer
n=49
print(solution(n))
