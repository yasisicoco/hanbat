from sys import stdin; input = stdin.readline
N = int(input())    # 배달해야 하는 설탕 키로수
num1 = num2 = num3 = int(1e9)
# N이 5의 배수라면
if N % 5 == 0:
    num1 = N // 5
# N이 3의 배수라면
elif N % 3 == 0:
    num2 = N // 3
# 5, 3 적절히 나누기
sugar = N   # 설탕 변수 생성
while sugar:
    if sugar < 3:
        num3 = int(1e9)
        break
    # while문 처음 들어왔으면 num3 변수 초기화
    if sugar == N:
        num3 = 0

    if sugar >= 5:
        sugar -= 5
        num3 += 1
    elif sugar >= 3:
        sugar -= 3
        num3 += 1

    if sugar % 5 == 0:
        num3 += sugar // 5
        sugar = 0
    elif sugar % 3 == 0:
        num3 += sugar // 3
        sugar = 0

# 그 중 최소 개수 구하기
ans = min(num1, num2, num3)
if ans == int(1e9):
    ans = -1
print(ans)

# 테케는 다 맞는데, 틀림.