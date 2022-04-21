import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(start, tree, parents):

    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)


n = int(input())
arr = [[] for _ in range(n+1)]
Parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(1, arr, Parents)

for i in range(2, n+1):
    print(Parents[i])
