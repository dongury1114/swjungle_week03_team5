import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

A = 'n'+input().strip() # 인덱스를 맞추기 위해 n 추가 

graph =[[] for _ in range (N + 1)]

for _ in range(N-1): # 반복 범위 잘 떠올리기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)

#실외에 맞닿아 있는 실내 점을 세주는 함수
def dfs(V):
    count = 0
    visited[V] = True
    for i in graph[V]:
        if A[i] == "1":
            count += 1
        elif A[i] == "0" and not visited[i]:
            count += dfs(i)

ans = 0
for i in range(1, N +1):
    if A[i] == '1':
        for j in graph[i]:
            if A[j] == "1":
                ans += 1
    
    else:
        if not visited[i]:
            tmp = dfs(i)
            ans += tmp * (tmp - 1)
print(ans)