W=int(input())
num5=W//5
L=[]
for i in range(num5+1):
    rem=W-i*5
    if(rem%3==0):
        L.append(i+(rem//3))
    else:
        continue
if(len(L)==0):
    print("-1")
else:
    print(min(L))