N=int(input())
for i in range(N):
    info=list(map(int,input().split()))
    classNum = info.pop(0)
    info.sort()
    maxGap=0
    for j in range(len(info)-1):
        if info[j+1]-info[j]>maxGap:
            maxGap=info[j+1]-info[j]
    print(f"Class {i+1}")
    print(f"Max {info[-1]}, Min {info[0]}, Largest gap {maxGap}")