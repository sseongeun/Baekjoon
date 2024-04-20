T=int(input())
for i in range(T):
    count=0
    s,f=map(int,input().split())
    for j in range(s,f+1):
        j=str(j)
        count+=j.count('0')
    print(count)