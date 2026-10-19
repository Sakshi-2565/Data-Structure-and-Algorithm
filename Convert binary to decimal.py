def binary2decimal(num):
    deci = 0
    power = 0
    index = len(num) - 1

    while index >= 0:
        x = int(num[index]) * (2**power)
        deci += x
        index -= 1
        power += 1
    return deci


B2D = binary2decimal("110010")
print(B2D)
