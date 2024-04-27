from itertools import permutations

N=int(input())
iter=list(map(str,input().split()))

def check(perm,iter):
    for i in range(len(iter)):
        if iter[i]==">" and perm[i]>perm[i+1]:
            continue
        elif iter[i]=="<" and perm[i]<perm[i+1]:
            continue
        else:
            return False
            
    return True


L=list(range(10))
result=[]
for perm in permutations(L,N+1):
    if check(perm,iter):
        result.append(perm)
    else:
        {}
        

print(''.join(str(num) for num in result[-1]))
print(''.join(str(num) for num in result[0]))
