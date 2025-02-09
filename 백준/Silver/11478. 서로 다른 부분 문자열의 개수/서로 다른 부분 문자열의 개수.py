s=list(input())
result=[]

for i in range(1,len(s)+1): # 길이(1~5)
    for j in range(0,len(s)-i+1): # 시작점
        curr= "".join(s[j:j+i])
        result.append(curr)
    
print(len(set(result)))