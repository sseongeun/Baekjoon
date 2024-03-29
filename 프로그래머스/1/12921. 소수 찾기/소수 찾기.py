def solution(n):
    result=0
    for i in range(2,n+1):
        IsPrime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                IsPrime=False
                break
            else:
                continue

        if IsPrime:
            result+=1
    return result