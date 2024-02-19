from itertools import permutations
N=int(input())
arr=list(map(int,input().split()))

all = permutations(arr)
sumL=[]
for L in all:
    
    sum=0
    for j in range(len(L)-1):
        sum=sum+abs(L[j]-L[j+1])
     
    sumL.append(sum)
print(max(sumL))