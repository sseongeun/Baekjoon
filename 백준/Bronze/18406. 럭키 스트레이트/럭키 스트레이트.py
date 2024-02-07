S=input()
S=list(S)
S=[int(ele)for ele in S]

pivot=len(S)//2
sum1,sum2=0,0
for i in range(pivot):
    sum1+=S[i]
    sum2+=S[i+pivot]
    
if(sum1==sum2):
    print("LUCKY")
else:
    print("READY")