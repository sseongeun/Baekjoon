
L=[]
while(True):
    L=input()
    if(L[0]=="#" and len(L)==1):
        break
    L=L.upper()
    L=list(L)
    
    count=0
    for i in L:
        if(i=="A"or i=="E"or i=="I"or i=="O"or i=="U"):
            count+=1
 
    print(count)