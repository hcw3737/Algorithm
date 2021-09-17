
# 광고 삽입
# 시간 제한 X, 완전탐색
def get_time(time) :
    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])
    second = int(time.split(":")[2])
    total = hour*3600+minute*60+second
    return total

def solution(play_time, adv_time, logs):
    answer = ''
    # finish = get_time(play_time)
    ad = get_time(adv_time)

    records = []
    for log in logs :
        start = get_time(log.split('-')[0])
        end = get_time(log.split('-')[1])
        play = end - start
        records.append([start, end, play, log.split('-')[0]]) #마지막:시작시간

    # play시간과 같은 경우
    if play_time == adv_time :
        return '00:00:00'

    records.sort(key=lambda x : (x[0],x[1])) # 정렬

    result = []
    # play시간과 다른 경우
    for s,e,p,t in records :
        end_time = s + ad
        sum = 0
        for s1,e1,p1,t1 in records :
            if end_time<s1:
                break
            elif e1<s :
                continue
            elif s<=e1 and e1<=end_time :
                if s1<=s:
                    time = e1-s
                elif s<s1:
                    time = e1 - s1
            elif s1<=end_time and end_time<e1:
                if s1<=s:
                    time = end_time-s
                elif s<s1:
                    time = end_time - s1
            else :
                continue
            sum+=time
        result.append(sum)

    idx = result.index(max(result))

    answer = records[idx][3]

    return answer
