import sys
input=sys.stdin.readline

N,M=map(int,input().split())
array=[]

def get_sum(array,i,j,x,y):
    total=0
    for row in range(i-1,x):
        total+=sum(array[row][j-1:y])
            
    return total
    

for _ in range(N):
    array.append(list(map(int,input().split())))
    
T=int(input())
for _ in range(T):
    i,j,x,y=map(int,input().split())
    print(get_sum(array,i,j,x,y))