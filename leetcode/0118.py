nums = [1,2,3,4]
k = 5
from collections import Counter
def maxOperations(nums,k) :
    answer = 0
    num_cnt = Counter(nums)
    num_list = sorted(Counter(nums))
    for i in num_list :
        j = k - i
        if i > j :
            break
        elif i == j :
            answer += num_cnt[i]//2
        elif j in num_list:
            answer += min(num_cnt[i],num_cnt[j])
    return answer

# nn = [2,2,3,3,3,4,4,4]
# nn.index(3)

digit_word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = [int(chr) for chr in input_string if chr.isdigit()]
digit_string = " ".join([digit_word[digit] for digit in digits])


underscore_str = "to_camel_case"
str_list = list(map(str,underscore_str.split('_')))
camelcase_str="".join


underscore_str = "__EXAMPLE__NAME__"
str_list = underscore_str.split('_')
camelcase_str = ''
for idx, word in enumerate(str_list) :
    word = word.lower()
    if idx > 0 :
        word = word.capitalize()
    camelcase_str+=word



