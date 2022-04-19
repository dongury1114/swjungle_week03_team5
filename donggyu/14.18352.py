from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
#모든 도시에 대한 최단 거리 초기화
visited = [-1] * (N+1)
visited[X] = 0

def bfs(X):
    que = deque([])
    que.append(X)
    visited[X] = 0
    while que:
        X = que.popleft()
        #현재 도시에서 이동할 수 있는 모든 도시 확인
        for i in graph[X]:
            # 아직 방문하지 않은 도시라면
            if visited[i] == -1:
                #최단 거리 갱신
                #현재 도시와 출발 도시 사이의 거리 + 1
                visited[i] = visited[X] + 1
                que.append(i)

bfs(X)
if K not in visited:
    print(-1)
else:
    for i in range(N+1):
        if visited[i] == K:
            print(i)

print(visited)
print(graph)


# que = deque([])

# def bfs(X):
#     que.append(X)
#     now = que.popleft()

#     for i in graph[now]:
#         if distance[i] == -1:
#             distance[i] = distance[now] + 1
#             que.append(i)


# check = False

# for i in range(1, N+1):
#     if distance[i] == K:
#         print(i)
#         check = True

# if check == False:
#     print(-1)

