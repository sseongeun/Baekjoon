from itertools import permutations

def solution(k, dungeons):
    result = []

    perm = list(permutations(dungeons,len(dungeons)))

    for i in perm:
        power = k
        curr =0 
        for j in i:
            if power >= j[0]:
                power-=j[1]
                curr+=1
            else:
                break
        result.append(curr)

    return max(result)