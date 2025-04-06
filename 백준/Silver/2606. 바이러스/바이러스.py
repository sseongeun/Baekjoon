def bfs(graph, visited, start):
    queue = [start]
    visited[start] = True
    cnt = 0

    while queue:
        curr = queue.pop(0)
        cnt += 1

        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return cnt

N = int(input())  # 컴퓨터 수
M = int(input())  # 연결 쌍 수

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)  # ✅ 올바른 초기화

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph, visited, 1) - 1)  # 1번 제외

