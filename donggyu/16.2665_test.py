from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]
visited[0][0] = 0

que = deque([])
que.append((0,0))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    while que:
        x, y = que.popleft()
        if x == n - 1 and y == n - 1: # 종료조건
            return visited[x][y] # 이해안됨 // visited: 검은방을 흰 방으로 바꾼 갯수
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny <n and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    que.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

print(bfs())

#BFS

#https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-2665%EB%B2%88-%EB%AF%B8%EB%A1%9C%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
#----------- 이해 어려움 ----------
# 1. 시작지점(0, 0)에서 bfs를 한다. (visited = 검은 방을 흰 방으로 바꾼 횟수)
#     - 해당 위치가 흰 방(1)이면 이전 visited의 값으로 초기화, appendleft(흰 방 먼저 탐색)
#     - 해당 위치가 검은 방(0)이면 이전 visited에서 1을 더해서 초기화, append
# 2. x, y 가 도착지점(N-1, N-1)이면 return visited[x][y]