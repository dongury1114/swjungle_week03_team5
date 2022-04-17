from collections import deque
import sys

sys.stdin = open("input.txt")
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#가로, 세로 받기
N, M = map(int, input().split())

#그래프 만들기
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0] * (M) for _ in range(N)]
que = deque([])
# que.append([0,0]) #que.append((0,0))

print(graph[3][4])
visited[0][0] = 1
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    que.append([x,y])
    while que:
        x, y = que.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= (N-1) and  0 <= ny <=(M-1) and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(bfs(0,0))
#다른 버전 끼리 아이디어가 완전 다른거 같은데, bfs 구조인것은 알겠다. 다른 아이디어 지만 둘다 bfs 인것은 같은가?