import math
def solution(progresses, speeds):
    stack=[]
    for i in range(len(progresses)):
        stack.append(math.ceil((100-progresses[i])/speeds[i]))


    first=stack.pop(0)
    count=1
    result=[]

    for i in stack:
        if first<i:
            result.append(count)
            first=i
            count=1
        else:
            count+=1
    result.append(count)
    
    return result