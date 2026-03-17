class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)

        def f(t):
            if t == 0:
                return 1
            if t < 0:
                return 0
            if dp[t] != -1:
                return dp[t]

            total = 0
            for num in nums:
                total += f(t - num)

            dp[t] = total
            return total

        return f(target)
        