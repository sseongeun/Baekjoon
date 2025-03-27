import heapq

def solution(scoville, K):
    scoville.sort()
    heapq.heapify(scoville)
    cnt=0
    
    
    while True:
        minNum = heapq.heappop(scoville)

        if minNum >=K:
            break

        elif minNum < K and len(scoville)==0:
            cnt=-1
            break

        else:
            nextNum = heapq.heappop(scoville)
            heapq.heappush(scoville, minNum+(nextNum*2))
            cnt+=1

    return cnt