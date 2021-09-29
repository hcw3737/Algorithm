# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    s_list = list(map(str, s.split(' ')))

    for ch in s_list :
        answer+=(ch.capitalize()+' ')
        
    return answer[:-1]
