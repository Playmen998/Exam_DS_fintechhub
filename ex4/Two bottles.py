import random


# val = int(input())
val = 20

a = 0  # A = 0
b = 0  # B = 0
c = 0  # оба по 0
for _ in range(100000):
    val_A = val_B = val
    while True:
        num = random.randint(0, 3)
        if num == 0:
            val_A = val_A - 20
            val_B = val_B - 70
        elif num == 1:
            val_A -= 50
            val_B -= 50
        elif num == 2:
            val_A -= 75
            val_B -= 25
        elif num == 3:
            val_A -= 100
            val_B -= 0
        if val_A <= 0:
            if val_B <= 0:
                val_B = 0
                c += 1
                break
            val_A = 0
            a += 1
            break
        elif val_B <= 0:
            val_B = 0
            b += 1
            break

sum = round((a / (a + b + c)) + ((0.5 * c) / (a + b + c)), 3)
print(sum)
