#안되면 쳐 외우기
#외않되
import sys
from heapq import heappush, heappop
sys.stdin = open("input.txt")

def dijkstra(start, end):
    heap = []
    heappush(heap, (0, start))  # 시작지점 힙에 추가
    distance = [sys.maxsize] * (N + 1)  # 각 정점사이의 거리 무한대로 초기화
    distance[start] = 0  # 시작 지점 0으로 초기화

    while heap:
        weight, index = heappop(heap)
        for e, c in bus[index]:
            if distance[e] > weight + c:
                distance[e] = weight + c
                heappush(heap, (weight + c, e))
    return distance[end]

# input(신선하게 어려웠다)
N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수
bus = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, input().split())  # 출발지, 도착지, 비용
    bus[start].append((end, cost))
start, end = map(int, input().split())  # 찾고자하는 비용 경로(출발지, 도착지)

# print
print(dijkstra(start, end))

# 다익스트라를 구현하면서 왜 우선순위 큐를 사용하는지 궁금하였다. bfs 대신에 다익스트라를 구현했다는 자체만으로도 엄청난 시간을 단축했다고 생각하였다. 
# 하지만 우선순위 큐를 사용하지 않으면 읽는 순서에 따라서 값 업데이트 수가 많을 수 있으며 굳이 하지 않아도 되는 연산들을 많이 하기 때문에 우선순위 큐를 활용해야 한다고 하였다.