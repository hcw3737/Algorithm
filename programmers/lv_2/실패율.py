from collections import Counter

def solution(N, stages):

    stage_dict = Counter(stages)
    user = len(stages)
    result = dict()
    for k in range(1,N+1):
        if k > N : continue
        else :
            if k not in stage_dict.keys() :
                result[k] = 0
            else :
                v = stage_dict[k]
                rate = v / user
                user -= v
                result[k] = rate

    result = sorted(result.items(), key = lambda x: x[1], reverse=True)
    answer = [k for k,v in result]
    return answer

