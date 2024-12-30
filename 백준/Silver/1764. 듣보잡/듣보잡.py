N,M=map(int,input().split())
nlist=[]
mlist=[]

for i in range(N):
    nlist.append(input())
    
for i in range(M):
    mlist.append(input())

result=list(set(nlist)&set(mlist))
result.sort()

print(len(result))
for i in result:
    print(i)