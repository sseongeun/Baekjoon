import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        minNum = heapq.heappop(scoville)
        if minNum >=K:
            break
        elif minNum < K and len(scoville)==0:
            answer=-1
            break
        else:
            secondMinNum = heapq.heappop(scoville)
            heapq.heappush(scoville,minNum+(secondMinNum*2))
            answer+=1
    return answer
    
    
    