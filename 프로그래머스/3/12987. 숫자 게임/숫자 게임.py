def solution(A, B):
    size=len(A)
    answer=0
    ap=0
    bp=0
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    while size>0:
        if A[ap]<B[bp]:
            answer+=1
            bp+=1
        ap+=1
        size-=1
        
    return answer
            
            
            
    
            
            
    return answer