def cal(xy,w,h):
    l=[]
    if xy[0]==1:
        return h+xy[1]
    elif xy[0]==2:
        return xy[1]
    elif xy[0]==3:
        return h-xy[1]
    else:
        return w+h-xy[1]
    
w,h=map(int,input().split())
length=h+w
storeNum=int(input())
locations=[]
for i in range(storeNum+1):
    xy=list(map(int,input().split()))
    position=[]
    position.append(xy[0])
    position.append(cal(xy,w,h))
    locations.append(position)
    
dong=locations.pop()
answer=0

for i in locations:
    if i[0]==dong[0] or abs(i[0]-dong[0])==2: 
        l=abs(i[1]-dong[1])
    else:
        l=abs(i[1]+dong[1])
        
    if l<=length:
        answer+=l
    else:
        answer+=(length*2-l)
    
print(answer)
