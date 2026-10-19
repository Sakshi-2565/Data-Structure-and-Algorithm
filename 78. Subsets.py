class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        total = 1 << n
        result = []

        for num in range(0, total):
            lst = []
            for i in range(0, n):
                if num & (1 << i) != 0:
                    lst.append(nums[i])
            result.append(lst)

        return result


s = Solution()
ss = s.subsets([1, 2, 3, 4, 5])
print(ss)
