n, k = map(int, input().split())

person = list(map(int, input().split()))
person.sort()

cnt = 0
hap = 0

while person:
    if len(person) == 1:
        cnt +=1
        break

    if person[0] - person[-1] > k:
        person.pop()
        cnt += 1
    else:
        person.pop(0)
        person.pop()
        cnt += 1

print(cnt)
