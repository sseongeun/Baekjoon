def gcd(x,y): #최대공약수, 유클리드 호제
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y    


a1,b1=map(int,input().split())
a2,b2=map(int,input().split())

up=a1*b2+a2*b1 #분자
down=b1*b2

gcd=gcd(up,down) # 최대공약수를 구해줌
print("{} {}".format(up//gcd,down//gcd))