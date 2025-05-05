row=[[] for _ in range(5)]
col=[[] for _ in range(5)]
ver1=[]
ver2=[]

dic={}
call=[]

for i in range(5):
    temp = (list(map(int,input().split())))
    for j in range(5):
        dic[temp[j]] = [i,j]
        
for _ in range(5):
    call+=list(map(int,input().split()))
        
for i in range(len(call)):
    location = dic[call[i]]
    row[location[0]].append(call[i])
    col[location[1]].append(call[i])
    
    if location[0]==location[1]:
        ver1.append(call[i])
    if location in [[0,4],[1,3],[2,2],[3,1],[4,0]]:
        ver2.append(call[i])

       
    cnt=0
    for r in row:
        if len(r)==5:
            cnt+=1
    for c in col:
        if len(c)==5:
            cnt+=1
    if len(ver1)==5:
        cnt+=1 
    if len(ver2)==5:
        cnt+=1 
        
    if cnt>=3:
        print(i+1)
        break