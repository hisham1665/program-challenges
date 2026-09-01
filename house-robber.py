def rob(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n) :
            dp[i] = max(dp[i-2] + nums[i] , dp[i-1])
        return dp[n-1]
