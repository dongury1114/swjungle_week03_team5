import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline


def dfs(start, end):
    visited[start][end] = True
    for i in range(4):
        nx, ny = dx[i] + start, dy[i] + end
        if 0 <= nx < n and 0 <= ny < m:
            if ice[nx][ny] == 0:
                if not visited[nx][ny] and ice[start][end] != 0:
                    ice[start][end] -= 1


n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

year = 0
cnt = 0

while True:
    year += 1
    visited = [[False] * (m) for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if not visited[i][j] and ice[i][j] != 0:
                # dfs(i, j)
                visited[i][j] = True
                for q in range(4):
                    nx, ny = dx[q] + i, dy[q] + j
                    if 0 <= nx < n and 0 <= ny < m:
                        if ice[nx][ny] == 0:
                            if not visited[nx][ny] and ice[i][j] != 0:
                                ice[i][j] -= 1

    visited = [[False] * (m) for _ in range(n)]

    for x in range(1, n):
        for y in range(1, m):
            if ice[x][y] != 0 and not visited[x][y]:
                cnt += 1
                if cnt == 2:
                    break

    if cnt > 1:  # 종료 조건
        break

    total = 0
    for i in ice:
        total += sum(i)
    if total == 0:
        print(0)
        exit()

print(year)
