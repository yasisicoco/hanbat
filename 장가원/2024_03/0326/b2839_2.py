from sys import stdin; input = stdin.readline
sugar = int(input())    # 배달해야 하는 설탕 kg수

# 최대한 5의 배수를 만들기 전략
bongji = 0  # 봉지 수
while sugar:    # sugar가 0이 될때까지 반복
    if sugar % 5 == 0:
        bongji += sugar // 5
        # 무조건 sugar = 0 이 됨 -> break
        break
    if sugar < 3:   # sugar 가 1kg or 2kg 남아있으면 배달 불가능
        bongji = -1
        break
    sugar -= 3      # sugar 가 5의 배수가 될때까지 3kg 씩 담기
    bongji += 1
print(bongji)
