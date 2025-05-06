N=int(input())
distance = list(map(int,input().split()))
cost = list(map(int,input().split()))



curr=cost[0]
total = curr*distance[0]
idx=1
cost.pop(0)


for i in cost:
    if i<=curr:
        curr=i
    total+=curr*distance[idx]
    idx+=1
    if idx==len(distance):
        break
        
print(total)