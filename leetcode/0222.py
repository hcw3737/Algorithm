# leetcode
from collections import Counter
def findLongestWord(s, d):
    max = 0
    answer = []
    for l in d :
        s_l = list(s)
        d_l = list(l)
        cnt = 0
        for i in d_l :
            if i in s_l:
                cnt+=1
                j = s_l.index(i)
                s_l = s_l
        if cnt > max:
            answer = []
            answer.append(l)
            max = cnt
        elif cnt == max :
            answer.append(l)
            max = cnt
    return sorted(answer)[0]



s = "abpcplea"
d = ["ale", "apple", "monkey", "plea"]
print(findLongestWord(s,d))
