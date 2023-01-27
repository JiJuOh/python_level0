# available at https://school.programmers.co.kr/learn/courses/30/lessons/120866
# The question is asking how many spots are safe from bombs.
# A bomb turns its surrounding spots into danger.
# The board is always a square, in range of 1 ≤ n ≤ 100

def solution(board):
    # part I
    bombs = []
    for x, i in enumerate(board):
        for y, j in enumerate(i):
            if(j==1):
                bombs.append((y,x))
    # part II           
    limit = len(board[0])-1
    danger = []
    for x,y in bombs:
        for a in range(x-1,x+2):
            for b in range(y-1,y+2):
                if(a>=0 and a<=limit and b>=0 and b<=limit):
                    danger.append((a,b))
                    # print(a,b)
    return((limit+1)**2 - len(set(danger)))

# My code consists of two parts.
# First part is for getting the coordinates of bombs and saving them in a list called bombs
# In the second part, with the information we got from part I, 
# we will save all available coordinates of dangerous spots  in the list called danger excluding spots out of the board.
# To return, we subtract the number of unique coordinates in danger from all the spots on board

# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.1MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10MB)
# 테스트 7 〉	통과 (0.05ms, 10.1MB)
# 테스트 8 〉	통과 (0.00ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.00ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10MB)
# 테스트 12 〉	통과 (0.01ms, 9.98MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.11ms, 10MB)


# One of the interesting solutions is like below
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
 
# I never thought about declaring set like line 34. should try later
# In the line 39, when if x(is true),when updating the danger set, the range of x and y can be written like this
# return the sum of the number of values that are valid.

# 테스트 1 〉	통과 (0.04ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.4MB)
# 테스트 5 〉	통과 (0.03ms, 9.99MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.02ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.12ms, 10.3MB)

# find out what makes difference
