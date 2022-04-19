import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

num = [i for i in range(0, 21)]

for _ in range(10):
    a, b = map(int, input().split())

#https://www.acmicpc.net/problem/10804



import sys

sys.stdin = open("input.txt")

N = input()
card = [0] * 10
count = 0

#같은 수가 있으면 갯수 count
#단 6 <-> 9

for i in N:
    if i == "6" or i == "9":
        count += 1
    else:
        card[int(i)] += 1

if count % 2 == 0:
    count = count // 2
else:
    count = count // 2 +1

card[6] = count

print(max(card))