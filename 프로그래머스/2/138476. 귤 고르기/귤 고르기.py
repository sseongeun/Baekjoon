from collections import Counter
def solution(k, tangerine):


    count = Counter(tangerine)

    sorted_tan = sorted(tangerine, key=lambda x: (-count[x], x))

    result=[]
    for i in range(k):
        result.append(sorted_tan[i])
        
    return len(set(result))