n = int(input())

box = list(map(int, input().split()))
box.sort()

m = int(input())
cnt = 0

for i in range(m):
    small = box[0]
    big = box[-1]
    small += 1
    big -= 1
    box[0] = small
    box[-1] = big
    box.sort()
    cnt += 1


print(abs(box[0] - box[-1]))
