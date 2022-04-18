import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline

V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
graph = [list(map(int, input().split())) for _ in range(E)]

graph.sort(key=lambda x: x[2]) # 가중치 순으로 정렬

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

print(Vroot)
print(find(3))
