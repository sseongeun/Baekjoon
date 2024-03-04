L=[]
for i in range(1,46):
    for j in range(i):
        L.append(i)

s,e=map(int,input().split())
print(sum(L[s-1:e]))