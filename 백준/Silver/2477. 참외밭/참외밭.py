garo=[]
sero=[]
total=[]
max_garo = 0
max_sero = 0
max_garo_index = 0
max_sero_index = 0

K=int(input())
for i in range(6):
    dir,length=map(int,input().split())
    if dir == 3 or dir ==4: # 세로
        if length>=max_sero:
            max_sero=length     
            max_sero_index=i    
    else:
        if length>=max_garo:
            max_garo=length
            max_garo_index=i
    total.append(length)
    
indexList=[ total[max_sero_index-1], max_sero, total[(max_sero_index+1)%6], total[max_garo_index-1],max_garo,total[(max_garo_index+1)%6]]
indexList=list(set(indexList))

result=1
for i in total:
    if i not in indexList:
        result*=i
        
print(K*(max_garo*max_sero- result))