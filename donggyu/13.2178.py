from collections import deque
import sys

sys.stdin = open("input.txt")
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range (N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que = deque([])


def bfs(x, y):
    
    que.append([x,y])
    while que:
        x ,y = que.popleft()

        for i in range(4):
            nx= dx[i] + x
            ny= dy[i] + y
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

    # 벽이므로 진행 불가
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny)) 
    return graph[N-1][M-1]

print(bfs(0,0))


# 참고: https://jokerldg.github.io/algorithm/2021/03/24/maze.html
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 1:
#             que.append([i,j])
# 