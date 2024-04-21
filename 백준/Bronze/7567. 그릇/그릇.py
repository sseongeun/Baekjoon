N=input()
N=[s for s in N]

start=N[0]
result=10
for i in range(1,len(N)):
    if N[i]==start:
        result+=5
    else:
        start=N[i]
        result+=10
print(result)