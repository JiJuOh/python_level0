# https://school.programmers.co.kr/learn/courses/30/lessons/120876
# We have to return the sum of length of overlapped lines.


# The first two defs were my first approach. However, I couldn't figure out why testcase 1,2 are failing.
# Except 1,2 the other test cases which were usually executed within 0.00ms .
# Since the length of lines is always 3, I thought it's better to deal this problem just with few tuples.

# def compareTwoLines(left, right) returns an overlapped part of two lines:left,right in a tuple.
# if there exists overlapped lines, return the info of that part otherwise return None
def compareTwoLines(left, right):
    if(left[1] >= right[0]):
        if(left[1]<= right[1]):
            return [right[0],left[1]]
        else:
            return[right[0],right[1]]
        
# since there are only three lines, I manually indicated the three lines.
# Then this def finds the two overlapped lines 
# after that, return overlapped length by the situation
def solution(lines):
    lines.sort()
    left = lines[0]
    middle = lines[1]
    right = lines[2]
    
    double1 = compareTwoLines(left,middle)
    double2 = compareTwoLines(middle,right)
    
    if(double1 is None):
        if(double2 is None):
            return 0
        else:
            return double2[1]-double2[0]
    else:
        if(double2 is None):
            return double1[1]-double1[0]
        else:
            if(double1 == double2):
                return double1[1]-double1[0]
            else:
                doublecheck = compareTwoLines(double1,double2)
                ans = double2[1]-double2[0]+ double1[1]-double1[0]
                if(doublecheck is None):
                    return ans
                else:    
                    return ans - (doublecheck[1]-doublecheck[0])
# 테스트 1 〉	실패 (0.00ms, 10.2MB)
# 테스트 2 〉	실패 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (0.00ms, 10.4MB)
# 테스트 6 〉	통과 (0.00ms, 10.3MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.00ms, 10.4MB)
# 테스트 9 〉	통과 (0.00ms, 10.3MB)
# 테스트 10 〉	통과 (0.00ms, 10.4MB)


# Secondly, I tried with count() method to solve all the testecases.
# It solved all the testcases but took pretty much longer time to execute.
# It put numbers, which meaning a "block" in a list called coords.
# I put all the available blocks from three lines,
# and made a set called index to count by unique value.
# so whenever count is more than 2, I added 1 to ans property.
# and return ans
def solution(lines):
    a = lines[0]
    b = lines[1]
    c = lines[2]
    coords = []

    for x in a,b,c:
        for i in range(x[0],x[1]):
            coords.append(i+1)

    index = set(coords)
    ans = 0
    for x in index:
        if (coords.count(x)>=2):
            ans += 1
            
    return ans
    
# 테스트 1 〉	통과 (0.47ms, 10.3MB)
# 테스트 2 〉	통과 (0.45ms, 10.4MB)
# 테스트 3 〉	통과 (0.01ms, 10MB)
# 테스트 4 〉	통과 (1.21ms, 10.2MB)
# 테스트 5 〉	통과 (0.10ms, 10.2MB)
# 테스트 6 〉	통과 (0.07ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (1.85ms, 10.3MB)
# 테스트 9 〉	통과 (0.13ms, 10.2MB)
# 테스트 10 〉	통과 (0.02ms, 9.99MB)


  
# Below is one of the answers of this problem.
# The last code is the key to solve this.
# return the union of the intersections of three lines
# set() automatically excluding the intersection of s1,s2 and s3
 def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.04ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.06ms, 10.4MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.4MB)
