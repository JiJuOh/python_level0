# yemaye가 안됨

def checkBabble(x):
    if "aya" in x:
        x= x.replace("aya"," ")
    if "ye" in x:
        x= x.replace("ye"," ")
    if "woo" in x:
        x= x.replace("woo"," ")
    if "ma" in x:
        x= x.replace("ma"," ")
    return x

def solution(babbling):
    speak = ["aya", "ye", "woo", "ma"]
    can = []
    checking = []
    for x in babbling:
        x = checkBabble(x)
        can.append(x)
    for x in can:
        x = checkBabble(x)
        checking.append(x.replace(" ", ""))
    
    return(checking.count(""))
  
# 테스트 1 〉	통과 (0.05ms, 10.3MB)
# 테스트 2 〉	통과 (0.08ms, 10.4MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.07ms, 10.4MB)
# 테스트 5 〉	통과 (0.11ms, 10.2MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.3MB)
# 테스트 8 〉	통과 (0.08ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.04ms, 10.4MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.02ms, 10.4MB)
# 테스트 16 〉	통과 (0.02ms, 10.3MB)
# 테스트 17 〉	통과 (0.03ms, 10.2MB)

def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
                b = b.replace(w, ' ', 1)
        if len(b.strip()) == 0:
            c += 1
    return c
  
# 테스트 1 〉	통과 (0.04ms, 10.1MB)
# 테스트 2 〉	통과 (0.14ms, 10.2MB)
# 테스트 3 〉	통과 (0.12ms, 10MB)
# 테스트 4 〉	통과 (0.11ms, 10.1MB)
# 테스트 5 〉	통과 (0.07ms, 10.1MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.05ms, 10.2MB)
# 테스트 8 〉	통과 (0.08ms, 10.1MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.02ms, 10.1MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)
# 테스트 17 〉	통과 (0.02ms, 10.2MB)
