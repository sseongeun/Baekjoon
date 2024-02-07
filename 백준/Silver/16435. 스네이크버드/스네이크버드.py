N,L=map(int,input().split())
F = list(map(int,input().split()))
F.sort()

for i in range(len(F)):
    if(L>=F[i]):
        L+=1
    else:
        break
    
print(L)