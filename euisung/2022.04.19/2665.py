import sys
from heapq import heappush, heappop
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline


def find():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    heap = []
    heappush(heap, [0, 0, 0])
    visit[0][0] = True

    while heap:
        a, x, y = heappop(heap)
        if x == n - 1 and y == n - 1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                visit[nx][ny] = True
                if board[nx][ny] == 0:
                    heappush(heap, [a + 1, nx, ny])
                else:
                    heappush(heap, [a, nx, ny])


n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]

find()
