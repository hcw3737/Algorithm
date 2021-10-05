
https://programmers.co.kr/learn/courses/30/lessons/77485

# 행렬 테두리 회전하기

def solution(rows, columns, queries):
    matrix = [[r*columns+c+1 for c in range(columns)] for r in range(rows)]
    result = list()

    # 회전하기
    for r1, c1, r2, c2 in queries :
        result.append(10000)
        item = matrix[r1-1][c1-1]
        # 왼->오
        for j in range(c1, c2) :
            matrix[r1-1][j], item = item, matrix[r1-1][j]
            result[-1] = min(result[-1], item)
        # 위->아래
        for i in range(r1, r2) :
            matrix[i][j], item = item, matrix[i][j]
            result[-1] = min(result[-1], item)
        # 오->왼
        for j in range(c2-2, c1-2, -1) :
            matrix[i][j], item = item, matrix[i][j]
            result[-1] = min(result[-1], item)
        # 아래->위
        for i in range(r2-2, r1-2, -1) :
            matrix[i][j], item = item, matrix[i][j]
            result[-1] = min(result[-1], item)

    return result
