arr = []
for i in range(40):
  if i % 2 == 0 :
      if i != 10 or i != 20 or i != 30 :
          arr[0].append(i + 2)
          arr[1].append(i + 4)
          arr[2].append(i + 6)
          arr[3].append(i + 8)
          arr[4].append(i + 10)

      else :
          arr[0].append(i + 2)
          arr[1].append(i + 4)
          arr[2].append(i + 6)
          arr[3].append(i + 8)
          arr[4].append(i + 10)

arr = []
for i in range(5):
    arr[i].append(i + 2)
    arr[i].append(i + 4)
    arr[i].append(i + 6)
    arr[i].append(i + 8)
    arr[i].append(i + 10)



arr = [0]*3

#
# def r( #파라미터 ):
#     # if 끝나는 조건 :
#     #   무엇을 해야할까?
#     #   return
#     for i in range( #어떤 숫자가 들어갈까? ):
#         # i 를 어디에 넣을까??
#         # r( ??? )
#

def r(N):
    # 끝나는 조건 재귀는 무조건 끝나는 조건이 있어야 돼!!
    if N == 10:
        # arr를 이용하는 함수
        print(arr)
        # return 바닥치고 올라와야지
        return

    # 중간 지점
    # 내가 현재 arr의 위치가 N이야
    # 근데 그러면 arr[N]에다 무엇을 넣을까??
    #
    for i in range(4):
        arr[N] = i
        r(N+1)

# N : 현재 arr의 위치
# i: 현재 arr의 위치에 들어갈 값
















ball = [0]*4

def r(N) :
    if N == 4 :
        print(ball)
        return

    for i in range(4) :
        ball[N] = i
        r(N+1)


r(0)

##############################################################3

import sys
input = sys.stdin.readline

ans = 0
dices = list(map(int,input().split()))
map1 = [
    [],
    [13,16,19],
    [22,24],
    [28,27,26],
    [25,30,35,40,0]
]

def solution(count,sub,position) :
    global ans
    if count == 9 and ans != 0 :
        if sub + 40 < ans :
            return
    elif count == 10 :
        if ans < sub :
            ans = sub
        return
    for i in range(4) :
        x,y = position[i]
        if x == 4 and y == 4 :
            continue
        nx,ny = position[i]
        if x == 0 :
            if y == 5 :
                nx = 1
                ny = -1
            elif y == 10 :
                nx = 2
                ny = -1
            elif y == 15:
                nx = 3
                ny =-1
            elif y == 20 :
                nx = 4
                ny = 3
        ny += dices[count]
        if nx == 0 and ny >= 20:
            nx = 4
            if ny == 20 :
                ny =3
            else :
                ny = 4
        elif 0 < nx < 4 and ny > len(map1[nx]) -1 :
            ny -= len(map1[nx])
            nx = 4
        elif nx == 4 and ny > 4 :
            ny = 4
        if map1[nx][ny] != 0 and [nx,ny] in position :
            continue
        position[i] = [nx,ny]
        solution(count+1,sub+map1[nx][ny],position)
        position[i] = [x,y]


for i in range(21) :
    map1[0].append(2*i)
stack = [[0,0, [[0,0] for _ in range(4)],[0]*4]]
solution(0, 0, [[0,0] for _ in range(4)])
print(ans)


