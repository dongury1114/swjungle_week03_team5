
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
M = int(input())


graph = []
visited = [False] * (N+1)

for i in range(N + 1 ):
    graph.append([])

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# # 준비작업 완료
# # dfs를 활용하여 1이랑 같은 덩어리 애들 count
count = 0
def dfs(v):
    global count
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
            count += 1

dfs(1)
print(count)