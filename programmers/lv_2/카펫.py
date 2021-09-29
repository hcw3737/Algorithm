# 카펫

# 카펫. 완전탐색

def solution(brown, yellow):
    # 노란색 사이즈 종류
    divide = []
    divide_back = []
    for i in range(1, int(yellow**(1/2))+1):
        if (yellow % i == 0) :
            divide.append(i)
            if (i != (yellow//i)):
                divide_back.append(yellow//i)

    size = divide + divide_back[::-1]

    # 노란색 사이즈 찾기
    for i in range(len(size)) :
        row = size[i]
        col = size[-(i+1)]
        if row > col:
            break
        # 브라운 사이즈와 일치
        if row+col+2 == brown//2 :
            return [col+2, row+2]


# 최적화

def solution(brown, yellow):
    # 노란색 사이즈 종류
    for i in range(1, int(yellow**(1/2))+1):
        if (yellow % i == 0) :
            row = i
            col = yellow//i
            if row+col+2 == brown//2 :
                return [col+2, row+2]
