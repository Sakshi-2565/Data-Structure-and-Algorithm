#################### Return True/False ########################


def func(index, total):
    if total == k:
        return True
    elif total > k:
        return False
    if index >= len(nums):
        return False
    Sum = total + nums[index]
    pick = func(index + 1, Sum)
    if pick == True:
        return True
    Sum = total
    not_pick = func(index + 1, Sum)
    return not_pick


k = 8
nums = [1, 2, 3]
print(func(0, 0))


####### Return One Subset also ######################


def func(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return True
    elif total > k:
        return False
    if index >= len(nums):
        return False
    subset.append(nums[index])
    Sum = total + nums[index]
    pick = func(index + 1, Sum, subset)
    if pick == True:
        return True
    e = subset.pop()
    Sum = total
    not_pick = func(index + 1, Sum, subset)
    return not_pick


result = []
k = 8
nums = [1, 2, 3, 4]
print(func(0, 0, []))
print(result)
