N=int(input())
L=[]
for i in range(N):
    L.append(int(input()))

if N==1:
    print("0")
else:

    me=L[0]
    rest=L[1::]
    count=0

    while me<=max(rest):
        m=max(rest)
        rest[rest.index(m)]-=1
        me+=1
        count+=1 
        
    print(count)