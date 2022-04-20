import sys


sys.stdin = open("input.txt")
sys.setrecursionlimit
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

print(graph)