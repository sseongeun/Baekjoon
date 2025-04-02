import heapq
import sys
input = sys.stdin.readline

N=int(input()) # 수업 개수
cnt=0
classes = []

for _ in range(N):
    classes.append(list(map(int,input().split()))) #시작시간, 종료시간
 
classes.sort() # 시작시간이 빠른 순으로 정렬
heap=[]
heapq.heappush(heap,classes[0][1])


# 이전 강의와 같은 강의실을 사용할 수 있다면 그냥 빼면된다
for i in range(1,N):
    if heap[0]<= classes[i][0]:
        heapq.heappop(heap) # 같은 강의실 재사용이 가능하다면 이전 수업을 제거한다
        
    heapq.heappush(heap,classes[i][1])
    
print(len(heap))