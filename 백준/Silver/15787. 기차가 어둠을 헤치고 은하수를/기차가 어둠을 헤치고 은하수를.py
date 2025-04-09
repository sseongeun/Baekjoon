import sys
input=sys.stdin.readline


N,M = map(int,input().split()) # 기차수, 명령수

trains = [[0 for _ in range(20)] for _ in range(N)]

for _ in range(M):
    oper = list(map(int,input().split()))
    
    if oper[0]==1:
        if trains[oper[1]-1][oper[2]-1]==0:
            trains[oper[1]-1][oper[2]-1]=1
    elif oper[0]==2:
        if trains[oper[1]-1][oper[2]-1]==1:
            trains[oper[1]-1][oper[2]-1]=0
    elif oper[0]==3:
        temp =trains[oper[1]-1][0:19]
        trains[oper[1]-1]=[0]+temp
    else:
        temp =trains[oper[1]-1][1:]
        temp.append(0)
        trains[oper[1]-1]=temp
 
dic={}    
cnt=0   
for train in trains:
    if str(train) in dic.keys():
        continue
    else:
        dic[str(train)]=1
        cnt+=1
        
print(cnt)