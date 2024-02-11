import sys
input=sys.stdin.readline

N=int(input()) # 명령어의 수 입력
Q=[]
for i in range(N):
    M=[]
    M=list(map(str,input().split()))
 
    
    if(M[0]=='push'):
        Q.append(M[1])
    elif(M[0]=='pop'):
        if(len(Q)==0):
            print("-1")
        else:
            print(Q[0])
            del Q[0]
    elif(M[0]=='size'):
        print(len(Q))
    
    elif(M[0]=='empty'):
        if(len(Q)==0):
            print("1")
        else:
            print("0")
    elif(M[0]=='front'):
        if(len(Q)==0):
            print("-1")
        else:
            print(Q[0])
    else: #back
        if(len(Q)==0):
            print("-1")
        else:
            print(Q[-1])