import math

def scoring(score) :
    if 90 <= score :
        return 'A'
    elif 80 <= score and score < 90 :
        return 'B'
    elif 70 <= score and score < 80 :
        return 'c'
    elif 60 <= score and score < 70 :
        return 'D'
    elif 50 <= score and score < 60 :
        return 'E'
    else :
        return 'F'


def test1(matrix) :
    answer = ''
    for j in range(len(matrix)):
        score = []
        for i in range(len(matrix)):
            score.append(matrix[i][j])

        if max(score) == matrix[j][j] :
            score.remove(max(score))
        elif min(score) == matrix[j][j] :
            score.remove(min(score))

        result = math.floor(sum(score)//len(score))
        answer+=scoring(result)

    return answer
