def fuc(L,N):
    new=[]
    for i in range(N):
        if L.count(L[i])!=1:
            new.append(0)
        else:
            new.append(L[i])
    return new

N=int(input())
scores=[]
L1,L2,L3=[],[],[]
for i in range(N):
    curr=list(map(int,input().split()))
    L1.append(curr[0])
    L2.append(curr[1])
    L3.append(curr[2])
    scores.append(curr)

r1=fuc(L1,N)
r2=fuc(L2,N)
r3=fuc(L3,N)
for i in range(N):
    print(r1[i]+r2[i]+r3[i])