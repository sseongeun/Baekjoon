X=int(input())
my=64
L=[0]


while(sum(L)!=X):
    
    if(X==64):
        break
    my=my//2
    back=my
    new=back
    L.pop()
    L.append(back)
    L.append(new)
    
    
    if(sum(L)-new>=X):
        L.pop()
    
    
    
print(len(L))