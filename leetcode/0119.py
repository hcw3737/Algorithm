#palindrome 회문문자열
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)-1,-1,-1):
            # 5글자일때 i=4이면, j=1 인덱스까지
            # print(i)
            j = len(s) - i
            for k in range(j):
                word = s[k:k+i+1]
                if self.palindrome(word) == True:
                    result = word
                    return result
                # print(s[k:k+i+1])
        return False

    def palindrome(self, word):
        for i in range(len(word)//2):
            if word[i] != word[len(word)-1-i]:
                return False

        return True


solution = Solution()
# solution.longestPalindrome()
s = "aacabdkacaa"
result = solution.longestPalindrome(s)

for i in range(len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        print("False")

    print("True")

## 1차 코드
#
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         s = s.lower()
#         s_list = []
#         for i in range(len(s)-1,-1,-1):
#             # 5글자일때 i=4이면, j=1 인덱스까지
#             # print(i)
#             j = len(s) - i
#             for k in range(j):
#                 s_list.append(s[k:k+i+1])
#                 # print(s[k:k+i+1])
#         for word in s_list :
#             if self.palindrome(word) == True :
#                 return word
#             else : continue
#         return word
#
#     def palindrome(self, word):
#         for i in range(len(word) // 2):
#             if word[i] != word[-1 - i]:
#                 return False
#
#             return True
