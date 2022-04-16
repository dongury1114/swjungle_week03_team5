n = int(input())

member = []

for i in range(n):
    height, weight = map(int, input().split())
    member.append((height, weight))

member.sort(reverse=True)

largest = 0
cnt = 0

for x, y in member:
    if y > largest:
        largest = y
        cnt += 1

print(cnt)
