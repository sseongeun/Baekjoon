N=int(input())
L=[]
for i in range(N):
    L.append(list(input()))
    
F=L[0]
for i in range(N-1):
    for j in range(len(F)):
        if(F[j]!=L[i+1][j]):
            F[j]="?"
            
print("".join(F))