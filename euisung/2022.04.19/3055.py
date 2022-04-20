import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(r)]
