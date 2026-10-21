############### Return Only True/False #######################

nums = [1, 2, 3, 4, 5, 6, 7]
k = 111


def backtrack(index, total):
    if total == k:
        return True
    elif total > k:
        return False
    if index >= len(nums):
        return False
    Sum = total + nums[index]
    pick = backtrack(index + 1, Sum)
    if pick == True:
        return True
    Sum = total
    not_pick = backtrack(index + 1, Sum)
    return not_pick


bt = backtrack(0, 0)
print(bt)

########### If True Return the subset #######################

nums = [1, 2, 3, 4, 5, 6, 7]
k = 11
result = []


def backtrack(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return True
    elif total > k:
        return False
    if index >= len(nums):
        return False
    subset.append(nums[index])
    Sum = total + nums[index]
    pick = backtrack(index + 1, Sum, subset)
    if pick == True:
        return True
    e = subset.pop()
    Sum = total
    not_pick = backtrack(index + 1, Sum, subset)
    return not_pick


bt = backtrack(0, 0, [])
print(bt)
print(result)
