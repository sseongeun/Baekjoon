dic={}
cnt=0

n= int(input())
for _ in range(n):
    cow_num, location = map(int,input().split())
    if cow_num not in dic.keys(): # 이전 내역이 없는 경우
        dic[cow_num]=location
    else: # 이전 내역이 있는 경우
        prev=dic[cow_num]
        if location != prev:
            cnt+=1
            dic[cow_num]=location
            
print(cnt)
            