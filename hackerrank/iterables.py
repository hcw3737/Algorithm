# https://www.hackerrank.com/contests/pythonist3/challenges/iterables-and-iterators/problem

from itertools import combinations

def solve(n, char, k):
    char = sorted(char)
    cnt = char.count('a')

    data = [i for i in range(len(char))]
    results = list(combinations(data, k))

    total = 0
    for result in results:
        if result[0] < cnt:
            total += 1

    exe = total / len(results)

    return round(exe, 3)


if __name__ == '__main__':
    n = int(input())
    char = list(map(str, input().split(' ')))
    k = int(input())

    print(solve(n, char, k))
