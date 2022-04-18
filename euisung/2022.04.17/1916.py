import sys
sys.stdin = open("input.txt", "r")

n = int(input())
m = int(input())

arr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())  # 출발, 도착, 비용
    arr[a].append([b, c])

start, end = map(int, input().split())

print(arr[1][1])
