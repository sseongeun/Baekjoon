S=input()
S=list(S)
S.append(S[-1])
a=-1
count=0
for i in range(1,len(S)):
    if(S[i]==S[i-1]):
        if(a==100):
            count=count+1
            a=-1
        else:
            continue
    else:
        S[i]=S[i-1]
        a=100
        
if(a==100):
    count=count+1
      
print(count)  