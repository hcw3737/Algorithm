from collections import Counter
import math

def solution(fees, records):
    answer = []

    car = []
    df = []

    for record in records :
        row = []
        row.append(int(record.split(" ")[0][:2])*60+int(record.split(" ")[0][3:]))
        row.append(record.split(" ")[1])
        car.append(record.split(" ")[1])
        row.append(record.split(" ")[2])
        df.append(row)

    df.sort(key=lambda x: (x[1], x[0]))

    car_num = Counter(car)

    results = []
    sum = 0
    for idx, data in enumerate(df) :
        if idx == 0 or data[1] != df[idx-1][1] :
            results.append(sum)
            if car_num[data[1]]%2==0:
                sum = 0
            else :
                sum = 23*60+59
        if data[2] == 'IN':
            sum-=data[0]
        else: sum+=data[0]

    results.append(sum)

    for result in results[1:] :
        if fees[0] >= result :
            answer.append(fees[1])
        else :
            fee = fees[1] + math.ceil((result-fees[0])/fees[2])*fees[3]
            answer.append(fee)

    return answer
