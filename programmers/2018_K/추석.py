# 추석 트래픽

def solution(lines):

    if len(lines) == 1 :
        return 1

    #시작시간 : 끝시간
    record = dict()
    for line in lines :
        info = line.split(" ")[1]
        second = float(line.split(" ")[2][:-1])
        time = list(map(float,info.split(":")))
        start = time[0]*3600+time[1]*60+time[2]
        end = round(start+second,3)
        record[start] = end

    #끝나는 시간 + 1초 구간별 개수
    result = []
    for s,e in record.items() :
        e_1 = e + 1.0
        cnt = 0
        for s1, e1 in record.items():
            # 2시작, 2끝 < 1끝 - 멈춤
            if e1<e:
                continue

            # 1끝+60<2시작 - 멈춤
            elif e_1<s1:
                break

            # 2시작<=1끝 경우
            elif s1<=e and e1>=e :
                cnt+=1

            # 1끝<2시작 경우
            elif e<s1 and s1<=e_1:
                cnt+=1

        result.append(cnt)

    return max(result)



lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]




