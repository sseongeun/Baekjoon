N,H,W = map(int,input().split())
graph=[]

for _ in range(H):
    graph.append(list(input()))
    
result=["?" for _ in range(N)]

for i in range(H):
    for j in range(N):
        # ?만 있으며 ?넣기
        # ?가 아닌 문자가 있다면 해당 문자를 넣기
        for k in range(W):
            if graph[i][W*j+k]!="?":
                result[j]=graph[i][W*j+k]
                break
    
print("".join(result))