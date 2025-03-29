from itertools import permutations

def solution(k, dungeons):
    perm = list(permutations(dungeons,len(dungeons)))
    result=[]
    for p in perm:
        temp = k
        cnt=0
        for i in p:
            if temp>=i[0]:
                temp-=i[1]
                cnt+=1
            else:
                break
        result.append(cnt)
        
    return(max(result))
        
        
        