import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def sol(node, start, end):

    for i in range(start + 1, end + 1):
        if node < arr[i]:
            node = arr[i]
            break 


arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

node = arr[0]
