#참여 리스트 PARTICIPANT
#완주 리스크 COMPLETION
#미완주 선수 이름 return

# def solution(participant, completion):
#     for i in range(len(participant)) :
#         cnt=0
#         for j in range(len(completion)) :
#             if participant[i] == completion[j] :
#                 del completion[j]
#                 #completion.remove(삭제할 원소)
#                 cnt+=1
#                 break
#         if cnt == 0 :
#             answer = participant[i]
#             break
#     answer = str(answer)
#     return answer

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)) :
        if i > (len(completion)-1) :
            answer = participant[i]
            break
        elif participant[i] != completion[i] :
            answer = participant[i]
            break
    return answer

#다른 사람 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

#다른 사람 풀이

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
