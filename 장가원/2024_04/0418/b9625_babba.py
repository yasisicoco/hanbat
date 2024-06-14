K = int(input())
# B -> BA, A -> B
word = 'A'
while K:
    new = []
    for i in range(len(word)):
        if word[i] == 'A':
            new.append('B')
        else:
            new.append('BA')
    word = ''
    for n in new:
        word += n
    K -= 1
print(word)
A = word.count('A')
B = word.count('B')
print(A, B)