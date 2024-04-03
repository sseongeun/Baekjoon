from itertools import combinations

def solution(nums):
    combs = list(combinations(nums, 3))

    L=[]
    for i in range(len(combs)):
        new=list(combs[i])
        L.append(sum(new))

    count=0  
    for i in L:
        isPrime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                isPrime=False
        if isPrime==True:
            count+=1
    return count