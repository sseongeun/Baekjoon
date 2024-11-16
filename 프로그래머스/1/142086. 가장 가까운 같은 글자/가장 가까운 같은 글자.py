def solution(s):
    data={}
    result=[]

    for i in range(len(s)):
        if s[i] not in data:
            data[s[i]]=i
            result.append(-1)
        else:
            result.append(i-data[s[i]])
            data[s[i]]=i
            
    return result
        