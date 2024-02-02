num=int(input())

numbers = list(map(int, input().split()))
maxNum=max(numbers)
sumNum=sum(numbers)

print(round(sumNum/maxNum*100/num,2))