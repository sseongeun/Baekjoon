import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    result=0
    
    while len(scoville) >1 :
        m1=heapq.heappop(scoville)
        
        if m1<K:
            m2=heapq.heappop(scoville)
            minNum=m1+m2*2
            heapq.heappush(scoville,minNum)
            result+=1
        else:
            break
        
    if scoville[0]<K:
            return -1
    else:
        return result