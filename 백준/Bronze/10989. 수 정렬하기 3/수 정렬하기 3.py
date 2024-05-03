import sys
input=sys.stdin.readline

N=int(input())
result=[0]*10001

for i in range(N):
    result[int(input())]+=1

for i in range(len(result)):
    for j in range(int(result[i])):
        print(i)
