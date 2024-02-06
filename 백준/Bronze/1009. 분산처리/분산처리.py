T=int(input())
    
for i in range(T):
    a,b=map(int,input().split())
    a=a%10
    if(a==1 or a==5 or a==6):
        print(a)
    elif(a==0):
        print(10)
    elif(a==4 or a==9):
        if(b%2==0):
            print(10-a)
        else:
            print(a)
    else:
        if(b%4==1):
            print(a)
        elif(b%4==2):
            print(a**2%10)
        elif(b%4==3):
            print(10-a)
        else:
            print(10-a**2%10)