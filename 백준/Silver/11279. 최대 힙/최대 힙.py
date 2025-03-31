import heapq
import sys
input = sys.stdin.readline

N=int(input())
num_list=[]
heapq.heapify(num_list)

for i in range(N):
    input_num = (-1)*int(input())
    
    if input_num == 0 and len(num_list)==0:
        print("0")
    elif input_num == 0:

        print((-1)*heapq.heappop(num_list))

    else:
        heapq.heappush(num_list,input_num)