def func(index, total):
    if total == k:
        return 1
    elif total > k:
        return 0
    if index >= len(nums):
        return 0
    Sum = total + nums[index]
    pick = func(index + 1, Sum)
    Sum = total
    not_pick = func(index + 1, Sum)
    return not_pick + pick


k = 8
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(func(0, 0))


# Time Complexity = O(2**N)
# Space Complexity = O(N)
