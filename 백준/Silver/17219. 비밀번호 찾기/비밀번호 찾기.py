web={}
N,M=map(int,input().split())
for i in range(N):
    w,p=map(str,input().split())
    web[w]=p
    
for i in range(M):
    w=input()
    print(web[w])