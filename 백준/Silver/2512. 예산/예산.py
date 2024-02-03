num1=int(input())
numbers = list(map(int, input().split()))
num2=int(input())

start,end=0,max(numbers)

while start<=end:
    mid=(start+end)//2
    sum=0
    for i in numbers:
        if i<=mid:
            sum+=i
        else:
            sum+=mid
    if sum<=num2:
        start=mid+1
    else:
        end=mid-1
        
print(end)