N=int(input())
nums=list(map(int,input().split()))

d=nums[:] # 초기에는, 지금까지 만들 수 있는 최대합이 자기 자신이니까!


for i in range(N):
    for j in range(i):
        if nums[j]<nums[i]:
            d[i]=max(d[i],d[j]+nums[i])
        

print(max(d))