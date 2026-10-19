class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        ans = start ^ goal
        for i in range(0, 31):
            if ans & (1 << i) != 0:
                count += 1
        return count


S = Solution()
mini = S.minBitFlips(10, 7)
print(mini)
