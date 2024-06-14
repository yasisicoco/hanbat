strings = list(input())
bomb = list(input())

# while True:
for string in strings:
    for i in range(len(bomb)):
        if string == bomb[i]:
            if bomb[i] == bomb[-1]:
                strings.pop(bomb[i])
            else:
                break
        else:
            break
    # else:
    #     break
print(strings)