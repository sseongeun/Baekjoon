from itertools import combinations

def solution(number):
    combi=list(combinations(number,3))

    count=0
    for i in combi:
        if sum(i)==0:
            count+=1

    return count