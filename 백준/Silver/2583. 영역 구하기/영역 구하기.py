from collections import deque

# 입력 받기
M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]  # 🔹 올바른 크기로 수정

# 직사각형 채우기 함수
def turn1(lx, ly, rx, ry, graph):
    for i in range(ly, ry):  # 🔹 범위 조정 (ry+1 → ry, rx+1 → rx)
        for j in range(lx, rx):
            graph[i][j] = 1

# 직사각형 정보 입력
for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    turn1(lx, ly, rx, ry, graph)

# DFS 탐색 함수
def dfs(graph, x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()
    q.append((x, y))
    graph[x][y] = 1  # 🔹 방문 처리
    area = 1  # 🔹 현재 영역 크기
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:  # 🔹 조건 수정
                graph[nx][ny] = 1
                q.append((nx, ny))
                area += 1  # 🔹 영역 크기 증가
                
    return area  # 🔹 탐색이 끝나면 영역 크기 반환

# 영역 개수 및 크기 저장
count = 0
result = []

for i in range(M):  # 🔹 `M` 범위로 수정
    for j in range(N):  # 🔹 `N` 범위로 수정
        if graph[i][j] == 0:
            result.append(dfs(graph, i, j))  # 🔹 올바른 매개변수 순서
            count += 1  # 🔹 영역 개수 증가

# 출력
print(count)
print(*sorted(result))  # 🔹 정렬하여 출력