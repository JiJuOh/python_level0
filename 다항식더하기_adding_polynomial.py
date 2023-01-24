# 프로그래머스 > 코딩테스트 연습 > 코딩테스트 입문 > 다항식 더하기
# -------------------1 차 가공-------------------
# 처음부터 모든 변수의 케이스를 종이에 적어두고 시작했어야 했어야 더욱 빨리 풀 수 있었을 것이다
# solution은 메인 함수인데 여기에서 인풋에서 필요한 정보를 골라내어서 x가 포함된 element는 상수만 one_x에 담아두었다
# 이 때 1x의 경우 x 로만 표현이 되어 1을 담을 수 있게 미리 치환을 해두었다.
# 상수만 있는 경우 constant에 넣어주었다.
# 이 리스트에서 sum()을 이용하여 x의 값과 상수의 값을 추출하였다.
# 굳이 리스트가 아니라 += 축적하여 더해주는 방식으로 했으면 더 효율이 좋았을 듯하다.
# -------------------2 차 가공-------------------
# setFormat()은 1차에서 가공된 두 값을 받아서 포맷에 맞게 출력할 수 있도록 하는 함수이다.
# 고려해야 할 것이 몇가지 있었다.
# x의 상수를 출력할 때 고려해야 할 것
#   1. 1x 일때 x 만출력
#   2. 0일 때 아무것도 출력하면 안됨
#   3. 그 외의 경우 값+'x' 를 붙여서 출력해야 함
# 상수를 출력할 때 고려해야 할 것
#   default: 상수가 0 일경우 아무것도 출력하지 않는다.
#   1. 0x였을 경우 " + "는 생략하고 상수만 출력
#   2. 0x가 아니면  " + " 와 함께 상수의 합을 출력



def setFormat(x_sum, c_sum) :
    x_result = ''
    if(x_sum == 1):
        x_result = "x"
    elif(x_sum == 0):
        x_result = ''
    else : x_result = str(x_sum)+"x" 
    c_result = ''
    if(x_sum != 0):
        if(c_sum > 0):
            c_result= " + " + str(c_sum)
    else:
        if(c_sum > 0):
            c_result= str(c_sum)
    return(x_result+c_result)


def solution(polynomial):
    one_x =[]
    constant = []

    for poly in polynomial.split(" "):
        if(poly.count('x')>0):
            if(poly=='x'):
                poly = 1
            else: poly = int(poly[:-1])
            one_x.append(poly)
        elif(poly.isdigit()):
            constant.append(int(poly))
        else: continue
    return setFormat(sum(one_x), sum(constant))
