def solution(n):
    l=[]
    while(n>=1):
        l.append(n%3)
        n=n//3

    l.reverse()
    sum=0
    for i in range(len(l)):
        sum+=(l[i]*3**i)
        
    return sum