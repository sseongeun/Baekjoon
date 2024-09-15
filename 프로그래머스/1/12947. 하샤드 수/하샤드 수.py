def solution(x):

    sum=0
    l=list(map(int,str(x)))
    
    for i in l:
        sum+=i
        
    if x%sum==0:
        return True
    else:
        return False
    