# i번째부터 j번까지 자르고
# 거기서 k번째 숫자 추출

array = [1, 5, 2, 6, 3, 7, 4]
commands = [list(map(int,input()))for _ in range(3)]


def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        l = []
        for j in range(commands[i][0]-1,commands[i][1]) : #2,5 면 1~4번까지
            l.append(array[j])
        l.sort()
        answer.append(l[commands[i][2]-1])      #3번째면 2를 넣어야함 인덱스.
    return answer

print(solution(array,commands))

#다른 사람 풀이

def solution1(array, commands):
    answer = []
    for command in commands :
        i,j,k = command             #리스트 값을 하나씩 저장 가능
        answer.append(list(sorted(array[i-1:j]))[k-1])
        print(answer)
    return answer

