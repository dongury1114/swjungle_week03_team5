import sys

sys.stdin = open("input.txt")
# default 값이 1000이다
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def post_order(start, end):
    # 역전시 리턴
    if start > end:
        return

    # 루트 노드
    root = pre_order[start]
    idx = start + 1

    # root보다 커지는 지점을 찾는 과정  
    # for문으로 찾으면 안된다. 아래서 설명  
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1

    # 왼쪽 서브트리
    post_order(start + 1, idx - 1)

    # 오른쪽 서브트리
    post_order(idx, end)

    # 후위순회이므로 제일 마지막에 찍으면 된다
    print(root)


pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    # try에서 예외 발생시 break 실행
    except:
        break

post_order(0, len(pre_order) - 1)




# 순회 문제는 순회마다 각 특징을 이용해서 루트를 뽑아낸다. -> 대부분 해결법이 함수의 인자로 각각의 시작, 끝 인덱스를 넘긴다.
# 트리의 순회 문제는 항상 함수로 시작과 끝을 받아서 알아낸 루트를 기준으로 왼쪽 서브트리와 오른쪽 서브트리를 나눠서 재귀호출을 하며 역전시 return한다.
# 전위, 후위, 중위 순회의 설계는 거의 똑같고 print로 찍어내는 위치만 다르다.

# 전위 순회는 루트, 왼쪽, 오른쪽 순이므로 루트 찍고 왼쪽 오른쪽 재귀호출
# 중위 순회는 왼쪽 루트 오른쪽 순이므로 왼쪽 재귀 호출 후 찍고 오른쪽 호출
# 후위 순회는 왼쪽 오른쪽 루트순이므로 왼쪽, 오른쪽 호출한 뒤 찍기

# https://backtony.github.io/algorithm/2021-02-18-algorithm-boj-class4-20/