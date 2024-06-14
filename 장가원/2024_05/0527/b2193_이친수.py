N = int(input())

def pinary(num):
    if num == 1 or num == 2:
        return 1
    return pinary(num - 1) + pinary(num - 2)

print(pinary(N))

# 1 : 1 => 1
# 2 : 10 => 1
# 3 : 100 101 => 2
# 4 : 1000 1001 1010 => 3
# 5 : 10000 10001 10010 10100 10101 => 5
# 6 : 100000 100001 100010 100100 100101 101000 101001 101010 => 8

# 시간초과