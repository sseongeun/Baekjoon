import heapq
n,m=map(int,input().split()) # 카드 개수, 카드 합체 횟수
cards = list(map(int,input().split())) # 카드 구성

heapq.heapify(cards)

for _ in range(m):
    min1= heapq.heappop(cards)
    min2= heapq.heappop(cards)
    
    heapq.heappush(cards,min1+min2)
    heapq.heappush(cards,min1+min2)


print(sum(cards))