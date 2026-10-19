class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans


s = Solution()
num = s.singleNumber([1, 1, 2, 2, 3, 4, 4, 5, 6, 5, 6])
print(num)
