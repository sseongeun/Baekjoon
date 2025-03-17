num = input()
numList = list(map(int,num))
sumOfNum = 0
cnt = 0

while len(numList)>=2:
    sumOfNum = sum(numList)
    numList = list(map(int,str(sumOfNum)))
    cnt+=1

print(cnt)    
if sum(numList)%3 == 0:
    print("YES")
else:
    print("NO")