N=int(input())
numbers=list(map(int,input().split()))
numbers.sort(reverse=True)
sum=0
for i in range(1,N+1):
    sum+=i*numbers[i-1]
print(sum)