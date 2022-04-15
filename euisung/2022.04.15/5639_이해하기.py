from curses import beep
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

number = []

def sol(start, end):

    if start >= end:
        return

    root = number[start]

    if number[end-1] <= root:
        sol(start+1, end)
        print(root)
        return

    idx = 0

    for i in range(start + 1, end):
        if number[i] > root:
            idx = i
            break

    sol(start + 1, idx)
    sol(idx, end)
    print(root)


while True:
    try:
        number.append(int(input()))
    except:
        break


sol(0, len(number))
