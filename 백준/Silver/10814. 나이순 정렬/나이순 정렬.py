N=int(input())
L={}
for i in range(N):
    age,name=input().split()
    age=int(age)
    if age in L:
        L[age].append(name)
    else:
        L[age]=[name]
        
KL=sorted(L.keys())
for key in KL:
    for value in L[key]:
        print(f"{key} {value}")