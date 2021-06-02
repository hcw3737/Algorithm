#N명 원생 - 키순
#k개의 조 - 조별 인원 동일X
#티셔츠 비용 max-min
#max-min 합들 최소

from itertools import combinations
from sys import stdin
input = stdin.readline

N, k = map(int, input().split())
h_list = list(map(int, input().split()))

h_list = sorted(h_list)

list(map(int, combinations(N-1,k-1)))
