import math
from itertools import permutations

def isPrime(num):
    if num ==1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num %i ==0:
            return False
    return True


def solution(numbers):
    cnt=0
    number_list = list(map(int,numbers))
    for i in range(1,len(number_list)+1):
        temp=list(permutations(number_list,i))
        temp = set(temp)
        for i in temp:
            if i[0]==0:
                continue
            num =int(''.join(map(str,i)))

            if isPrime(num):
                cnt+=1
    return cnt