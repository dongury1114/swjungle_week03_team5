import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def topology():
    result = []
    que = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)

    while que:
        now = que.popleft()
        result.append(now)

        for i in student[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                que.append(i)
        print(now, end=' ')


n, m = map(int, input().split())
arr = []
student = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    arr.append([a, b])
    student[a].append(b)
    indegree[b] += 1

topology()
