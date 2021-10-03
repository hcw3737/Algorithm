https://programmers.co.kr/learn/courses/30/lessons/42578
    
# 위장 # 해시 # 42578

def solution(clothes):
    cloth = dict()
    for info in clothes :
        if info[1] in cloth.keys():
            cloth[info[1]]+=1
        else :
            cloth[info[1]] = 1

    case = 1
    for i in cloth.values():
        case *= (i+1)

    return case - 1
