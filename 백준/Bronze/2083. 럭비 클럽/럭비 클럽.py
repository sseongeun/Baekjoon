while(True):
    L=input().split()
    if(L[0]=='#'):
        break
    if(int(L[1])>17 or int(L[2])>=80):
        print(L[0]+" Senior")
    else:
        print(L[0]+" Junior")