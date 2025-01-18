a,b=map(str,input().split())

if len(a)>len(b):
    less = b
    big = a
else:
    less = a
    big = b
    
diff= len(big)-len(less) # 둘의 차이

result=[]
for i in range(diff+1):
    sum=0
    for j in range(i,i+len(less)):
        if less[j-i]==big[j]:
            sum+=1
    result.append(sum)

print(len(less)-max(result))