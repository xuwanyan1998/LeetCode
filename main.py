class Solution:
    def longestArithSeqLength(self, nums) -> int:
        dp = dict()

        for cur in range(len(nums)):
            for prev in range(cur):
                diff = nums[cur] - nums[prev]
                dp[(cur, diff)] = dp.get((prev, diff), 1) + 1
        for d in dp:
            if dp[d] == max(dp.values()):
                end, diff = d
                ans = []
                for i in range(end,-1,-1):
                    if (nums[end] - nums[i]) % diff == 0:
                        ans.append(nums[i])
                ans.sort()
                return ans

nums = [20,1,15,3,10,5,8]
print(Solution().longestArithSeqLength(sorted(nums)))