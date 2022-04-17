import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < N) and (0 <= ny <M):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)

T = int(input())#테스트케이스 개수
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[False] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        m, n = map(int, input().split())
        graph[n][m] = True

    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                dfs(i,j)
                count += 1
    print(count)
