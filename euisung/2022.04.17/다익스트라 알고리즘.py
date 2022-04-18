from heapq import heappush, heappop
import sys
input = sys.stdin.readline
infinity = int(2e9)


def Dijkstra(start):
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])

    while heap:
        w, n = heappop(heap)
        if dp[n] < w:
            continue
        for x, y in arr[n]:
            z = w + y
            if dp[x] > z:
                dp[x] = z
                heappush(heap, [z, x])


n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
dp = [infinity for i in range(n+1)]

for i in range(m):
    start_p, end_p, cost = map(int, input().split())
    arr[start_p].append([end_p, cost])

start, end = map(int, input().split())

Dijkstra(start)
print(dp[end])
