string=list(input())
dic={}

for i in range(97,123):
    dic[i]=0
    
for s in string:
    dic[ord(s)]+=1
    
print(*list(dic.values()))