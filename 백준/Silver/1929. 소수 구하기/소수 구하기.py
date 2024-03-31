start,end=map(int,input().split())

        
for i in range(start,end+1):
    if i==1:
        continue
    isPrime=True
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            isPrime=False
            break
    if isPrime:
        print(i)
        