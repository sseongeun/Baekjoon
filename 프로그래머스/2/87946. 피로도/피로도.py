from itertools import permutations

def solution(k, dungeons):
    perm=permutations(dungeons)
    result=[]
    c=k

    for i in perm:
        turn=0
        k=c
        for j in i:
            if k>=j[0]:
                k-=j[1]
                turn+=1
            else:
                break
        result.append(turn)

    return max(result)
