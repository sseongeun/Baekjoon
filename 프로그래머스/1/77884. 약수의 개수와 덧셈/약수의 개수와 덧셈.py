import math

def func(num):
    maxNum=int(math.sqrt(num))
    count=[]
    for i in range(1,maxNum+1):
        if num%i==0:
            count.append(i)
            count.append(num//i)
            
    count=list(set(count))
    if len(count)%2==0:
        return True
    return False


def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if func(i):
            answer+=i
        else:
            answer-=i
            
    return answer


        