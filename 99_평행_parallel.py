# https://school.programmers.co.kr/learn/courses/30/lessons/120875
# return 1 if there were paralleled lines among combinations of 4 dots.
# Otherwise, return 0

# below is my code
# getAngle gets an angle from two coordinates (a,b), (c,d)
# in the solution class, combinations of 4 dots are generated and their angle is appended to a list
# when the number of unique properties is not 6, it returns 1. since it means there were the same angles.
def getAngle(a,b,c,d):
    return (d - b)/(c - a)

def solution(dots):
    angles=[]
    for x in range(0,3): # 0, 1, 2
        for y in range(1,4): # 1, 2, 3
            if(x != y and x<y):
                angles.append(getAngle(dots[x][0],dots[x][1],dots[y][0],dots[y][1]))
    if(len(set(angles))!=6): return(1)
    return(0)
  
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)


# Below is one of the code of other answers.
# 1. from itertools import combinations : we can use combination function like this
# 2. we dont need to check all the list nor convert it to a set. if we find a*d = c*b during a for-loop, we can return 1 right after
from itertools import combinations
def solution(dots):
    a = []
    for (x1,y1),(x2,y2) in combinations(dots,2):
        a.append((y2-y1,x2-x1))
    for (x1,y1),(x2,y2) in combinations(a,2):
        if x1*y2==x2*y1:
            return 1
    return 0
  
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.00ms, 10.2MB)
