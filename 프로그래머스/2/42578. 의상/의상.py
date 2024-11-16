def solution(clothes):
    
    comb={}

    for i in clothes:
        if i[1] not in comb:
            comb[i[1]]=1
        else:
            comb[i[1]]+=1


    nums=comb.values()
    list(nums)

    result=1
    for i in nums:
        result*=(i+1)
    
    return result-1