N=int(input())
dic={}

for _ in range(N):
    file = list(map(str,input().split(".")))
    
    if file[1] not in dic.keys():
        dic[file[1]]=1
    else:
        dic[file[1]]+=1
        
dic =dict(sorted(dic.items()))

for i in dic.items():
    print(i[0],i[1])

        