import sys
input=sys.stdin.readline

n1=int(input())
n2=int(input())
n3=int(input())
num=n1*n2*n3
num=str(num)
for i in range(10):
    print(num.count(str(i)))