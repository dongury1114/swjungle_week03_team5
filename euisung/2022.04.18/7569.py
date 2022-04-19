import sys
from collections import deque
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def bfs():
    que = deque([])
    for i in range(m):
        for j in range(n):
            for x in range(k):
                i = i*x
                if box[i][j] == 1:
                    que.append([i, j])
    while que:
        x, y = que.popleft()
        for i in range(4):
            for w in range(k):
                nx, ny = dx[i] + (x*w), dy[i] + (y*w)
                if 0 <= nx < m and 0 <= ny < n and box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    que.append([nx, ny])


n, m, k = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

bfs()
print(box)

for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    count = max(count, max(i))

print(count - 1)
