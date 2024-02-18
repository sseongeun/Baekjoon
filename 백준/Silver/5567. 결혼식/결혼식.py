import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
L=[]
f1=[]
for i in range(m):
    new=list(map(int,input().split()))
    L.append(new)
    if(new[0]==1 or new[1]==1):
        f1.append(new[0])
        f1.append(new[1])

f2=[]
for i in L:
    if(i[0] in f1 or i[1] in f1):
        f2.append(i[0])
        f2.append(i[1])
    
print(len(set(f2+f1)-{1}))