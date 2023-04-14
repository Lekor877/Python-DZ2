S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))

for X in range(1, 1001):
    for Y in range(1, 1001):
        if X + Y == S and X * Y == P:
            print("Числа, которые задумал Петя: ", X, " и ", Y)
            break
    else:
        continue
    break
else:
    print("Петя ошибся, такие числа не существуют.")