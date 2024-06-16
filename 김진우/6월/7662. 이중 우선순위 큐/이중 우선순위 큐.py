# 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터중 하나를 삭제
# 두가지 연산이 사용
# 1. 데이터 삽입 연산
# 2. 데이터 삭제 연산
#   2-1. 우선순위가 가장 높은 것을 삭제
#   2.2. 우선순위가 가장 낮은 것을 삭제
# 최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력
import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    entry_finder = {}
    counter = 0

    k = int(input())
    for _ in range(k):
        cal, num = input().split()
        num = int(num)
        if cal == 'I':
            heapq.heappush(min_heap, (num, counter))
            heapq.heappush(max_heap, (-num, counter))
            entry_finder[counter] = num
            counter += 1
        elif cal == 'D' and num == 1:
            # 최대값 삭제
            while max_heap and max_heap[0][1] not in entry_finder:
                heapq.heappop(max_heap)
            if max_heap:
                _, idx = heapq.heappop(max_heap)
                del entry_finder[idx]
        elif cal == 'D' and num == -1:
            # 최소값 삭제
            while min_heap and min_heap[0][1] not in entry_finder:
                heapq.heappop(min_heap)
            if min_heap:
                _, idx = heapq.heappop(min_heap)
                del entry_finder[idx]

    # 힙에서 삭제된 값들 제거
    while max_heap and max_heap[0][1] not in entry_finder:
        heapq.heappop(max_heap)
    while min_heap and min_heap[0][1] not in entry_finder:
        heapq.heappop(min_heap)

    if entry_finder:
        print(f'{-max_heap[0][0]} {min_heap[0][0]}')
    else:
        print('EMPTY')