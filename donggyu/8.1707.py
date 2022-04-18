import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")
input = sys.stdin.readline


K = int(input()) #테스트 케이스의 갯수

graph=[]

for i in range(N+1):
    graph.append([])

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)