from collections import deque

def solution(cacheSize, cities):
    cache=deque(list([0]*cacheSize))
    total=0

    for i in cities:
        i=i.lower()
        if cacheSize == 0 :
            return 5*len(cities)
        else:
            if i in cache:
                cache.remove(i)
                cache.append(i)
                total+=1

            else:
                if cache:
                    cache.popleft()   
                cache.append(i)
                total+=5
            
    return total