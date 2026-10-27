def solve(ind, total, bracket, result):
    bracket = bracket
    result = result
    if ind >= len(bracket):
        if total == 0:
            result.append("".join(bracket))
        return
    if total > len(bracket) // 2:
        return
    elif total < 0:
        return
    bracket[ind] = "("
    Sum = total + 1
    solve(ind + 1, Sum, bracket, result)
    bracket[ind] = ")"
    Sum = total - 1
    solve(ind + 1, Sum, bracket, result)


n = 3
result = []
bracket = [""] * (2 * n)
solve(0, 0, bracket, result)
print(result)
