from collections import Counter

def solution(want, number, discount):
    cate=dict(zip(want,number))
    cate=dict(sorted(cate.items()))
    
    result=0
    for i in range(0,len(discount)-9):
        arr=discount[i:i+10]
        arr=Counter(arr)
        arr=dict(sorted(arr.items()))
        
        if cate == arr:
            result+=1
    
    return result
    