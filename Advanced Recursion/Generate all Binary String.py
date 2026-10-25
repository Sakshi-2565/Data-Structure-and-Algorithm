def solve(index, flag, num, result):
    if index >= len(num):
        result.append("".join(num))
        return result
    num[index] = "0"
    solve(index + 1, True, num, result)
    if flag == True:
        num[index] = "1"
        solve(index + 1, False, num, result)
        num[index] = "0"
    return result


n = 4
num = ["0"] * n
bin = solve(0, True, num, [])
print(bin)
