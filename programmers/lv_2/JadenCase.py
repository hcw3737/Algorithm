# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    s_list = list(map(str, s.split(' ')))

    for ch in s_list :
        answer+=(ch.capitalize()+' ') #첫단어 대문자, 나머지 소문자
        
    return answer[:-1]
