import math
def solution(n):
    answer = -1
    for i in range(int(math.sqrt(n)),-1,-1):
        if i**2 == n:
            return (i+1)**2
        else:
            return answer
      