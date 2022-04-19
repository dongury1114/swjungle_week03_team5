from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline # 리스트 만들때는 split() 처럼 strip()을 까먹지 않고 써줘야함

N = int(input())

#그래프 만들기 두개 다 기억해두기 // 언제든지 기억 나는걸로 바로 쓰기 위해 
graph = [list(map(int, input().strip())) for _ in range(N)]
# graph = []
# for i in range(N):
#     graph.append(list(map(int, input().strip())))
visited = [[-1] * N for _ in range(N)]
visited[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
que = deque([])
que.append((0, 0))
def bfs():
    while que:
        x, y = que.popleft()
        if x == N-1 and y == N-1:
            return visited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    que.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
print(bfs())