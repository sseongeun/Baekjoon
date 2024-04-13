T=int(input())
for i in range(T):
    L=list(map(int,input().split()))
    L.sort(reverse=True)
    print(L[2])
    