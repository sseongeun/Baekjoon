n=input().split('-')

l=[]
for i in n:
    sum=0
    temp=i.split('+')
    for j in temp:
        sum+=int(j)
    l.append(sum)

    
if n[0]=='-':
    start=(-1)*int(l.pop(0))
else:
    start=int(l.pop(0))

answer=start
for i in l:
    answer-=i
    
print(answer)