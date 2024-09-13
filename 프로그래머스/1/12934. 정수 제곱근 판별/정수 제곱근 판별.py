import math
def solution(n):
    answer=-1
    for i in range(int(math.sqrt(n))+1,-1,-1):
        if(n==i**2):
            answer=(i+1)**2
            break 
    return answer