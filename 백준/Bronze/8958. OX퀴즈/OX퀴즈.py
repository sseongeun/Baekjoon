def check(L):
    cur=0
    sum=0
    for i in range(len(L)):
        if(L[i]=="O"):
            cur+=1
            sum+=cur
        else:
            cur=0
    return sum


N=int(input())
for i in range(N):
    L=input()
    L=list(L)
    print(check(L))
    