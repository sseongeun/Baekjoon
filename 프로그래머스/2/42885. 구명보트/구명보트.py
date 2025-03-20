def solution(people, limit):
    people.sort()
    start=0
    last=len(people)-1
    result =0
    
    while(start<=last):
        if (people[start]+people[last]<=limit):
            start+=1
            last-=1
        else:
            last-=1
            
        result+=1
        
    return result
            
    