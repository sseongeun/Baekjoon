import sys
input=sys.stdin.readline

N=int(input())
L=[]
for i in range(N):
    L.append(int(input()))
    
L=sorted(L,reverse=False)

for i in L:
    print(i)