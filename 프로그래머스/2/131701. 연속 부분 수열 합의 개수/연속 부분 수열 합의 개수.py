def solution(elements):
    n=len(elements)
    result = []
    for i in range(n):
        elements.append(elements[i])
        for j in range(n):
            result.append(sum(elements[j:j+i+1]))
        
    
    
    result=list(set(result))
    return len(result)