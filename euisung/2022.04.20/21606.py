import sys
from collections import deque
sys.setrecursionlimit(10 ** 8)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

line = [0] + list(map(int, input().rstrip()))
Loot = [[] * (n+1)]
visited = [False]*(n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    Loot[a].append(b)
    Loot[b].append(a)


print(line)
