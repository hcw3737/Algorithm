# 체격순
# 앞뒤로만 빌려줄수 있음
# 최대한 많은 학생이 체육복 가지게
# 전체 학생 수 n
# lost 도난학생번호
# reserve 여벌 학생 번호
# 최대 학생수 리턴
# 여벌 있던 학생 중 도난 당하면 못 빌려줌

n = int(input())
reserve = list(map(int,input()))
lost = list(map(int,input()))

def solution(n, lost, reserve):
    answer = 0
    #여벌 개수 리스트 생성
    cnt = [1]*n
    for i in reserve :
        cnt[i-1] = 2
    # 먼저 여벌 학생에서 도난당한 학생 제외
    for a in lost :
        if a in reserve :
            cnt[a-1] = 1
        else : cnt[a-1] = 0

    for a in lost :
        #2번 학생은 1번 3번한테 빌릴수 있는데, 3번한테 빌리면 4번이 3한테 못빌림
        #따라서 만약 리스트가 순서대로면, 둘중 작은애한테 빌림
        if cnt[a-1] == 1 :
            continue
        elif cnt[a-2] == 2 :
            cnt[a-2] = 1
            cnt[a-1] = 1
        elif cnt[a] == 2 :
            cnt[a] = 1
            cnt[a-1] = 1

    #sum(cnt)        #리스트 내 합계
    #체육복 가지고 있는 학생수 카운트
    for i in range(len(cnt)):
        if cnt[i] != 0 :
            answer+=1
    return answer

#풀이
def solution(n,lost,reserve) :
    set_reserve = list(set(reserve) - set(lost))      #여벌학생-도난학생
    set_lost = list(set(lost)-set(reserve))          #도난학생리스트에서 여벌학생 제외
    set_lost.sort()
    set_reserve.sort()
    for i in set_reserve :
        if i-1 in set_lost :
            set_lost.remove(i-1)
        elif i+1 in set_lost :
            set_lost.remove(i+1)
    return n-len(set_lost)                      #최종 도난학생 리스트 빼기

#n에서 도난 학생 수 빼면 식이 간단해짐!!!
