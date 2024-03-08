import math

def solution(n):
    answer = []
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):
            answer.append(i)
            answer.append(n//i)
    answer=set(answer)       
    return sum(answer)