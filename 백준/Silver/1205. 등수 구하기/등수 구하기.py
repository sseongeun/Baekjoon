N,T,P = map(int,input().split())
if N!=0:
    scores = list(map(int,input().split()))
else:
    print("1")
    exit()
    
scores.append(T)
scores.sort(reverse=True)

if len(scores)>P:
    if scores[-1]==T:
        print("-1")
        exit()
    scores.pop()
    
for i in range(len(scores)):
    if scores[i]==T:
        print(i+1)
        break