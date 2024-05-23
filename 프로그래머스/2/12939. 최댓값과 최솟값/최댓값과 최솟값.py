def solution(s):
    s=list(map(int,s.split()))
    maxNum=str(max(s))
    minNum=str(min(s))
    return minNum+" "+maxNum