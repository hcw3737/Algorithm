# 복호화 암호화

def test2(sentence, keyword, skip) :
    answer = ''
    keywords = keyword*1000

    char = list(map(str, sentence))
    key = list(map(str, keywords))

    for idx, s in enumerate(skip) :
        #skip==0인경우
        if idx == 0 :
            answer+=key.pop(0)
            continue

        word1 = key.pop(0)
        for _ in range(s):
            if len(char) != 0 :
                word2 = char.pop(0)
                #같은 경우 뒤에
                if word2 == word1 :
                    answer+=word2
                    break
                else :
                    answer+=word2
            elif len(char) == 0:
                return answer
        answer+=word1

        #skip마지막
        if idx == len(skip)-1 :
            answer+=''.join(char)
            break
    return answer


