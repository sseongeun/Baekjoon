from itertools import combinations

N,M = map(int,input().split()) # 회원수 , 치킨 종류수

chicken =[i for i in range(M)]
flavor=[]
for i in range(N):
    flavor.append(list(map(int,input().split())))
    
comb = list(combinations(chicken,3))

sum_list=[]
for c in comb:
    sum=0
    for f in flavor:
        sum+=max(f[c[0]],f[c[1]],f[c[2]])
    sum_list.append(sum)
    
print(max(sum_list))