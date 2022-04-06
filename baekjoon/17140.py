from collections import Counter
import numpy as np


def row_func(graph):
    board = []
    max = 0
    for i in range(len(graph)):
        result = []
        for k,v in Counter(graph[i]).items():
            if k==0:
                continue
            result.append([k,v])

        result.sort(key=lambda x:(x[1],[0]))
        result = np.array(result).flatten()

        if len(result) > max :
            max = len(result)

        result = ''.join(list(map(str,result)))
        board.append(result)

    # 0 padding
    for i in range(len(board)):
        board[i] = list(map(int,board[i].ljust(max,'0')))

    graph = board
    return graph


def main():
    r, c, k = map(int, input().split())
    graph = []

    # import copy
    # graph2 = copy.deepcopy(graph)

    for _ in range(3):
        line = list(map(int, input().split()))
        graph.append(line)

    time = 0
    while graph[r-1][c-1] != k:
        time+=1
        if time<=10 :
            # R연산
            if len(graph)>=len(graph[0]):
                graph = row_func(graph)
                print(graph)
            # C연산
            else:
                # transpose
                np.transpose(graph)
                graph = np.transpose(row_func(graph))

        else:
            return -1
          
    return time

print(main())
