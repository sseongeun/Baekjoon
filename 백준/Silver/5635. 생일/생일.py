N=int(input())
L=[]
for i in range(N):
    curr=list(map(str,input().split()))
    curr=curr[::-1]
    curr.append(float(curr[0])+0.01*float(curr[1])+0.0001*float(curr[2]))
    L.append(curr)
sorted_list=sorted(L,key=lambda x:x[4])
print(sorted_list[N-1][3])
print(sorted_list[0][3])