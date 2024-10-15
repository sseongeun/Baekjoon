from collections import Counter
def solution(topping):
    p1=Counter(topping)
    p2=set()
    result=0

    for i in topping:
        p1[i]-=1
        p2.add(i)
        if  p1[i]==0:
            p1.pop(i)

        if len(p1) == len(p2):
            result+=1

    return result
    