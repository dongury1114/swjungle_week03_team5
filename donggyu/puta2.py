import sys

sys.stdin = open("input.txt")

N = input()

card = [0] * 10

#같은 수가 있으면 갯수 count
#단 6 <-> 9
count = 0
for i in N:
    if N == "6" or N == "9":
        count += 1
    else:
        card[int(i)] = 1

if count % 2 == 0:
    count = count // 2
else:
    count = count // 2 +1

card[6] = count
print(max(card))