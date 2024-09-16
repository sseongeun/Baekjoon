import math
import itertools


def checkPrime(n):
    num=int(math.sqrt(n))
    if n<2:
        return False
    for i in range(2,num+1):
        if n%i==0:
            return False
    return True

def solution(numbers):
    numList=list(map(str,numbers))
    answer=[]
    result=[]

    for i in range(1,len(numbers)+1):
        answer.extend(itertools.permutations(numList,i))
        result=set([int("".join(i)) for i in answer])


    final=0
    for j in result:
        if checkPrime(j):
            final+=1
            
    return final