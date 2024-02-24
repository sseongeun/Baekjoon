S,K=map(int,input().split())
min=S//K
    
L=[min]*K
i=0
while(sum(L)!=S):
    L[i]=L[i]+1
    i+=1
    
mul=1    
for i in range(K):
     mul*=L[i] 
print(mul)