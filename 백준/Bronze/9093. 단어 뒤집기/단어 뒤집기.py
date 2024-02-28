N=int(input())
L=[]
for i in range(N):
    L.append(list(map(str,input().split())))

    
for i in range(N):
    for j in range(len(L[i])):
        L[i][j]=L[i][j][::-1]
    print(*L[i])
