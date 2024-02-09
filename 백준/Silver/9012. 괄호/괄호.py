num=int(input())
L=[]
for i in range(num):
    L.append(list(input()))

for i in range(num):
    R=[]
    for j in range(len(L[i])):
        if(L[i][0]==")"):
            R.append(")")
            break     
        elif(L[i][j]==")" and len(R)==0):
            R.append(")") 
            break
        elif(L[i][j]=="("):
            R.append("(")
        else:
            R.pop()  
            
           
    if(len(R)==0):    
        print("YES")
    else:
        print("NO")