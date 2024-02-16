voca={}
N=input()
N=list(N)


for i in N:
    i=i.upper()
    if(i in voca):
        voca[i]=voca[i]+1
    else:
        voca[i]=1


max_value=max(voca.values())
max_keys=[key for key, value in voca.items() if value==max_value]

if(len(max_keys)==1):
    print(max_keys[0])
else:
    print("?")