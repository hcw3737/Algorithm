# s

ord('a')
ord('A')

s = str(input())
def solution(s):
    s = list(map(str,s))
    for i in range(len(s)) :
        s[i] = (s[i],ord(s[i]))
    l = sorted(s,key=lambda x:x[1],reverse = True)  #내림차순
    answer = ''
    for a in l :
        answer += a[0]
    return answer

print(solution(s))

## 다른 사람 풀이

def solution(s) :
    return ''.join(sorted,s,reverse=True)

def solution(s) :
    s = list(s)     #문자열내 문자 리스트화
    # s = list(map(str,s)) 이문자의 간편화

    s.sort(reverse = True)
    #sort하면 알아서 유니코드 값에 따라 정렬해줌

    answer = ''
    for i in s :
        answer += i     #문자도 +가 가능
    return answer
