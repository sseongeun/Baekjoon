from collections import deque

def solution(maps):
    answer=0
    rows=len(maps)
    col=len(maps[0])
    
    def bfs(x,y):
        dx=[0,0,1,-1] #오른쪽, 왼쪽, 위, 아래
        dy=[1,-1,0,0]

        queue=deque()
        queue.append((x, y))
        
        while queue:
            x,y=queue.popleft()
            for i in range(4):
        
                nx=x + dx[i]
                ny=y + dy[i]

                if nx<0 or nx>=rows or ny<0 or ny>=col:
                    continue

                if maps[nx][ny]==0:
                    continue

                if maps[nx][ny]==1:
                    queue.append((nx,ny))  
                    maps[nx][ny]=maps[x][y]+1

        return maps[-1][-1]
        
        
    
    answer = bfs(0, 0)
    if answer == 1:
        return -1
    return answer