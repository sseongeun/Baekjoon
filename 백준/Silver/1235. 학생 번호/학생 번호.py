k=int(input())
nums=[]
for i in range(k):
    n=input()
    nums.append(n)
  
i=1 
while True:
    L=[]
    for j in range(k):
        L.append(nums[j][-i:])
 
    if len(set(L))==k:
        print(i)
        break
    i+=1