A,B,V=map(int,input().split())
i=round((V-A)/(A-B))

while(True):
    if i>=((V-A)/(A-B)):
        i+=1
        break
    else:
        i+=1
print(i)