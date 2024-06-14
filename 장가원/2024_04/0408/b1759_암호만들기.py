from sys import stdin; input = stdin.readline
# 알파벳 C 가지로 L 개의 구성
L, C = map(int, input().split())
alphabets = list(input().split())
# 알파벳 사전순
alphabets.sort()
# 최소 한 개의 모음vowel, 최소 두 개의 자음consonant 으로 구성 (중복 x)
vowel = 'aeiou'
v_num = c_num = 0
def select(code):
    global v_num, c_num
    if len(code) == L:
        if v_num >= 1 and c_num >= 2:
            print(''.join(code))
        return
    start_idx = 0
    if code:
        start_idx = alphabets.index(code[-1]) + 1
    for num in range(start_idx, C):
        code.append(alphabets[num])
        if alphabets[num] in vowel:
            v_num += 1
        else:
            c_num += 1
        select(code)
        if code[-1] in vowel:
            v_num -= 1
        else:
            c_num -= 1
        code.pop()

select([])

'''
4 6
a t c i s w
a c i s t w
'''