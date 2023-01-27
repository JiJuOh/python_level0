def solution(common):
    last = common[-1]
    second = common[-2]
    if(second == 0):
        rate = 0
    else :
        rate = last/second
    add = last-second
    if(common[-3] * rate ==  second):
        return int(last * rate)
    else:
        return int(last+add)

# 조건중 common의 길이는 3이상 이어서 자주 쓰일 매개변수 맨 마지막, 맨마지막에서 두번째. 
# 각각 last, second를 생성해 주었습니다
# element 중 0 이 있어서 나누기 했을 때 런타임 에러를 방지하기 위해 분모를 쓸 second 에 방어장치?를 해둡니다
# 어차피 second가 0면 등비가 0은 등비수열 이니까요
# 조건문은 맨 마지막에서 세번째 수에서 등비를 곱했을 때 맨 마지막 수가 나오는지 안나오는 지로 체크해서
# int를 씌워서 내보냅니다
