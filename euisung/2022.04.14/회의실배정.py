
n = int(input())
time = []

for i in range(n):
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key=lambda x: (x[1], x[0]))
end_time = 0
start_time = 0
cnt = 0
for start, end in time:
    if start >= end_time:
        end_time = end
        cnt += 1
print(cnt)
