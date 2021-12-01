https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3

def solution(lottos, win_nums):
    cnt = 0
    sum = 0
    for lotto in lottos:
        if lotto == 0:
            cnt+=1
            continue
        else :
            if lotto in win_nums:
                sum+=1
                
    answer = []
    win = [sum+cnt, sum]
    
    for num in win :
        if num == 6:
            answer.append(1)
        elif num == 5:
            answer.append(2)
        elif num == 4:
            answer.append(3)
        elif num == 3:
            answer.append(4)
        elif num == 2:
            answer.append(5)
        elif num <= 1:
            answer.append(6)
        
    return answer
