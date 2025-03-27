def solution(clothes):
    category={}
    
    for cloth in clothes:
        if cloth[1] in category.keys():
            category[cloth[1]].append(cloth[0])
        else:
            category[cloth[1]]=[]
            category[cloth[1]].append(cloth[0])
        

    nums=[]
    for i in category:
        nums.append(len(category.get(i)))

    sum=1
    for i in nums:
        sum*=(i+1)
    
    return sum-1