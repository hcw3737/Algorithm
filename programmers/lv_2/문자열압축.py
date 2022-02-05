def solution(s):
    # answer = dict()
    # sentence = list(s)

    for num in range(1,len(s)//2+1):
        char = ''
        prev = s[:num]
        cnt = 1

        for j in range(num,len(s), num):
            if prev == s[j:j+num]:
                cnt+=1
            else :
                char += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j+num]
                cnt = 1

        char += str(cnt) + prev if cnt >=2 else prev

        answer = min(answer, len(char))

    return answer
