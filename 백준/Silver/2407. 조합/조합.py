N,M=map(int,input().split())
dic={}
for i in range(N+1):
    for j in range(i+1):
        if j==0:
            dic[(i,j)]=1
        elif j==i:
            dic[(i,j)]=1
        else:
            dic[(i,j)]= dic[(i-1,j-1)]+ dic[(i-1,j)]
            
print(dic[(N,M)])