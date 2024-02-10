L=[]
for i in range(10):
    n=int(input())
    L.append(n%42)
    
print(len(set(L)))