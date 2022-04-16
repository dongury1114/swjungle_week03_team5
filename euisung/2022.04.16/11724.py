import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(start, tree, parents):

    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)

n = int(input())

Tree = [[] for _ in range(n+1)]

Parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)


dfs(1, Tree, Parents)

for i in range(2, n+1):
    print(Parents[i])
