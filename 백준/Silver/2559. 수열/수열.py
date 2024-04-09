import sys
input=sys.stdin.readline

N,K=map(int,input().split())
L=list(map(int,input().split()))
result=[]
curr=sum(L[0:K])
result.append(curr)
for i in range(0,N-K):
    curr=curr-L[i]+L[i+K]
    result.append(curr)

print(max(result))