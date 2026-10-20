##############  BRUTE FORCE ########################


nums = [1, 2, 3]
result = []


def func(index, subset, target):
    if index >= len(nums):
        if sum(subset) == target:
            result.append(subset.copy())
        return

    subset.append(nums[index])
    func(index + 1, subset, target)
    subset.pop()
    func(index + 1, subset, target)


func(0, [], 3)
print(result)


##############  OPTIMAL SOLUTION  ########################


nums = [1, 2, 3]
result = []
k = 3


def backtrack(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return
    elif total > k:
        return
    if index >= len(nums):
        return

    subset.append(nums[index])
    Sum = total + nums[index]
    backtrack(index + 1, Sum, subset)
    e = subset.pop()
    Sum -= e
    backtrack(index + 1, Sum, subset)


backtrack(0, 0, [])
print(result)
