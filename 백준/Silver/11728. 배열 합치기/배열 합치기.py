import sys
input=sys.stdin.readline

A,B=map(int,input().split())
LA=list(map(int,input().split()))
LB=list(map(int,input().split()))
LA=LA+LB
LA.sort()
print(*LA)