import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

num = [i for i in range(0, 21)]

for _ in range(10):
    a, b = map(int, input().split())
