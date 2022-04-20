#완전탐색이라서 일단 접근 조차 틀ㅣ것 같ㅡㅁ
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

h = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(1,n): #범위 설정 부터문제 // 조건문으로 이전에 자기보다 뒤의 인덱스만 탐색?
        # if h[i] > h[j]:
        #     h[i] <= h[j]
        #     count += 1
        #     break

        # # elif h[i] <= h[j]
        # #     count += 1
        if h[i] <= h[j]:
            count += 1

print(count)