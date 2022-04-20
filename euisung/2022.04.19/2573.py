import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

year = 0

while True:
    year += 1
    count_water = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if ice[nx][ny] == 0:
                            count_water[i][j] += 1

    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0:
                ice[i][j] -= count_water[i][j]
                if ice[i][j] < 0:
                    ice[i][j] = 0

    visited = [[False] * (m) for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and ice[i][j] != 0:
                visited[i][j] = True
                arr = [[i, j]]
                while arr:
                    p = arr.pop()
                    for q in range(4):
                        nx, ny = dx[q] + p[0], dy[q] + p[1]
                        if 0 <= nx < n and 0 <= ny < m:
                            if ice[nx][ny] == 0:
                                if not visited[nx][ny] and ice[i][j] > 0:
                                    cnt += 1
                                    visited[nx][ny]

    if cnt > 1:
        break

    total = 0
    for i in ice:
        total += sum(i)

    if total == 0:
        print(0)
        exit()
print(year)
