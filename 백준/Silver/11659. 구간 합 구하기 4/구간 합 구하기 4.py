import sys
input=sys.stdin.readline

N,M=map(int,input().split())
L=list(map(int,input().split()))

for i in range(N-1):
    L[i+1]=L[i]+L[i+1]
    
L=[0]+L   

for i in range(M):
    start,end=map(int,input().split())
    print(L[end]-L[start-1])