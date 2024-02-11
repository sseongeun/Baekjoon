import sys
input=sys.stdin.readline

N=int(input()) # 명령어의 수 입력
L=[]
for i in range(N):
    M=[]
    M=list(map(str,input().split()))
 
    
    if(M[0]=='push'):
        L.append(M[1])
    elif(M[0]=='pop'):
        if(len(L)==0):
            print("-1")
        else:
            print(L[-1])
            L.pop()
    elif(M[0]=='size'):
        print(len(L))
    
    elif(M[0]=='empty'):
        if(len(L)==0):
            print("1")
        else:
            print("0")
    
    else: #top
        if(len(L)==0):
            print("-1")
        else:
            print(L[-1])