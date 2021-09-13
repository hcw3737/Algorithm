from collections import Counter

def solution(id_list, report, k):
    answer = []

    reports = set(report)
    report_id = [[] for _ in range(len(id_list))]

    count_id = []

    for info in reports :
        id = info.split(" ")[0]
        num = id_list.index(id)
        report_id[num].append(info.split(" ")[1])

        count_id.append(info.split(" ")[1])

    result = Counter(count_id)

    result_id = [key for key, value in result.items() if value >= k]

    for l in report_id:
        cnt = 0
        for id in l :
            if id in result_id:
                cnt+=1
        answer.append(cnt)

    return answer
