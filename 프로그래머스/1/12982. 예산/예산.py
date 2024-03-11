def solution(d, budget):
    d.sort()
    sum=0
    count=0
    for i in range(len(d)):
        if sum+d[i]>budget:
            break
        elif sum+d[i]==budget:
            count=i+1
            break
        else:
            sum+=d[i]
            count+=1
    return(count)