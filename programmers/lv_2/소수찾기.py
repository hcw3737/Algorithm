def solution(numbers) :
    numb = list(map(int, numbers))
    p_list = []
    for i in range(len(numb)):  # 0~1
        p_list += (list(permutations(numb, i + 1)))
    #숫자 순열
    s_list = set()
    for i in p_list:
        j = 0
        s_make = ''
        while j < len(i):
            s_make += i[j]
            j += 1
        s_list.add(int(s_make))
    s_list = list(s_list)

    answer = []
    for i in s_list:
        if i == 1 or i == 0:
            continue
        cnt = 0
        for x in range(1, i + 1):
            if i % x == 0:
                cnt += 1
        if cnt == 2:
            answer.append(i)
    return len(answer)
