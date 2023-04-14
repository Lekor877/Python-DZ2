n = int(input("Введите количество монет: "))
coins = input("Введите порядок монет (H или T без пробелов): ")

heads = 0
for c in coins:
    if c == 'H':
        heads += 1

tails = n - heads

if heads < tails:
    flips = heads
else:
    flips = tails

print("Минимальное количество монет, которые нужно перевернуть:", flips)