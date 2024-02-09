from itertools import combinations
nums=[]
while(True):
    num=list(map(int,input().split()))
    if(num[0]==0):
        break
    nums.append(num)

for i in range(len(nums)):
    for i in combinations(nums[i][1:],6):
        print(*i,sep=" ")
    print(" ")