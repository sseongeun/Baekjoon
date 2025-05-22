N=int(input())
cnt=0
dic={}

for _ in range(N):
    num,loc = map(int,input().split())
    if num not in dic.keys():
        dic[num]=loc
    elif loc != dic[num]:
        cnt+=1
        dic[num]=loc
        
print(cnt)