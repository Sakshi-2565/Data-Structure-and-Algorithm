def integer2binary(num):
    result = ""
    while num > 0:
        if num % 2 == 1:
            result += "1"
        else:
            result += "0"
        num = num // 2
    result = result[::-1]
    return result


i2b = integer2binary(13)
print(i2b)
