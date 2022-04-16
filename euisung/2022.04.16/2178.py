from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def sol(x, y):
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

      # 벽이므로 진행 불가
        if graph[nx][ny] == 0:
            continue

      # 벽이 아니므로 이동
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

  # 마지막 값에서 카운트 값을 뽑는다.
    return graph[n-1][m-1]


print(sol(0, 0))
