def solution(arr):
    result=[]
    prev=arr[0]
    result.append(prev)
    for i in range(1,len(arr)):
        if arr[i]!=prev:
            result.append(arr[i])
            prev=arr[i]
        
    return result