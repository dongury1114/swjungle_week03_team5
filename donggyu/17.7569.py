# 2차원 토마토를 풀고 문제를 읽고나니 3차원 배열을 구현해서 돌려야 겠다는 생각을 함

from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N, H = map(int, input().split())


graph = [[list(map(int, input().split())) for _ in range(N)] for _ in  range(H)]

que = deque([])

dx, dy, dz = [-1, 1, 0, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

res = 0

# for 문 순서에서 헷갈렸음 항상 신경쓰기
# 1이 저장되어 있는 좌표를 찾아 q에 저장
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                que.append([i,j,k])


def bfs():
    while que:
        z, x, y = que.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # try:

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and graph[nz][nx][ny] == 0:


                graph[nz][nx][ny] = graph[z][x][y] + 1
                que.append([nz, nx, ny])
            # except:
            #     print('asdfasdf')

bfs()

for i in range (H):
    for j in range (N):
        for k in range (M):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0) # 2번에서는 break로 문제가 없었는데, 이번 문제에서는 문제가 생김...(추가 공부하기)
            res = max(graph[i][j][k], res)

print(res - 1)