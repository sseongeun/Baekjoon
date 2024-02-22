num,total=map(int,input().split())
L=[]
for i in range(num):
    L.append(int(input()))
    
L.sort(reverse=True)


sum=0
for i in L:
    sum1=total//i
    total=total-i*sum1
    sum+=sum1
    
print(sum)