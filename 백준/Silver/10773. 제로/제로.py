num=int(input())
L=[]
for i in range(num):
    N=int(input())
    if(N==0):
        L.pop()
    else:
        L.append(N)
    

print(sum(L))   