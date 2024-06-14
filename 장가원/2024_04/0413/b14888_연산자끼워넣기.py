from sys import stdin; input = stdin.readline
N = int(input())        # 숫자 개수
numbers = list(map(int, input().split()))   # 숫자 리스트
operators = list(map(int, input().split())) # 연산자 수 + - * /

# 만들 수 있는 식의 결과 중 최댓값, 최솟값 출력.
# 답은 -10억 이상 10억 이하 (10의 10승)
MIN = int(1e10)
MAX = int(-1e10)

def make(i, number):
    global operators, MIN, MAX
    if i == N:
        MIN = min(MIN, number)
        MAX = max(MAX, number)
        return
    # 더하기
    if operators[0]:
        operators[0] -= 1
        make(i + 1, number + numbers[i])
        operators[0] += 1
    # 빼기
    if operators[1]:
        operators[1] -= 1
        make(i + 1, number - numbers[i])
        operators[1] += 1
    # 곱하기
    if operators[2]:
        operators[2] -= 1
        make(i + 1, number * numbers[i])
        operators[2] += 1
    # 나누기
    if operators[3]:
        operators[3] -= 1
        make(i + 1, int(number / numbers[i]))
        operators[3] += 1

make(1, numbers[0])

print(MAX)
print(MIN)
