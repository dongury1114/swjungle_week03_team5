#dfs, 백트래킹 문제
import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)

#참고: https://chul2-ing.tistory.com/67
#max, min: 선언부 범위 // dfs 냅부 div 선언시 int(a/b) 신경쓰기