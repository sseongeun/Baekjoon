from itertools import combinations

def solution(nums):
    
    temp = set(nums)
    tempSize = len(temp)
    
    if tempSize>= (len(nums)//2):
        return len(nums)//2
    else:
        return tempSize