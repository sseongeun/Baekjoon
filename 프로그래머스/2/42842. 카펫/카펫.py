import math

def solution(brown, yellow):
    for i in range(1,int(math.sqrt(yellow))+1):
        if yellow%i==0:
            saro=i
            garo=yellow//i

            if (2*(saro+garo+2))==brown:
                return [garo+2,saro+2]
