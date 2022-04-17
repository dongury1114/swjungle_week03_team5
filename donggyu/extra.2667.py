import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")
# input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# graph = [[0]*n for _ in range(n)]
# for i in range(n): 
#     line = input() 
#     for j, b in enumerate(line): 
#         graph[i][j] = int(b)

visited = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0] #좌우
dy = [0, 0, 1, -1] #상하
count = 0
def dfs(x, y):
    global count
    visited[x][y] = True
    if graph[x][y] == 1:
        count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny <n:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                dfs(nx, ny)

housing = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            dfs(i,j)
            housing.append(count)
            count = 0

housing.sort()
print(len(housing))
for i in housing:
    print(i)