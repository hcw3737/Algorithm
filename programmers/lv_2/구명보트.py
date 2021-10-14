#구명보트 다시 풀어보기
def boat(people,limit) :
    p_list = sorted(people)
    save = []
    sum = len(people)
    cnt = 0
    while len(save) != sum :
        if len(p_list) == 1 :
            save.append(p_list.pop(0))
        elif p_list[0]+p_list[-1] > limit :
            save.append(p_list.pop(-1))
        else :
            save.append(p_list.pop(0))
            save.append(p_list.pop(-1))
        cnt+=1
        
# 해답
def solution(people, limit):
    people.sort(reverse=True)
    answer = len(people)
    s, e = 0, len(people)-1
    while s<e :
        if people[s]+people[e] <= limit :
            e-=1
            answer-=1
        s+=1
    #따로 pop, remove이런거 하지 않고 순차적으로 계산 진행
    return answer
