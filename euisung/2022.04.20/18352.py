import sys
from collections import deque
sys.setrecursionlimit(10 ** 4)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(start):
    answer = []
    que = deque([start])
    visited[start] = True
    distance[start] = 0
    while que:
        now = que.popleft()  # 현재 위치
        for i in city[now]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')


# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())
city = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

bfs(x)
