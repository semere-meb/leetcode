class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] +1)
        return max(dp)


# if __name__ == "__main__":
#     l = [0,1,0,3,2,3]
#     print(l)
#     print(Solution().lengthOfLIS(l))
