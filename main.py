class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        if sum(nums) % k != 0: return False
        target = sum(nums) / k
        nums.sort(reverse=True)
        if nums[0] > target: return False
        bucket = [0] * k

        def backtrack(index, bucket):
            if index == len(nums):
                for i in range(k):
                    if bucket[i] != target: return False
                return True

            for i in range(k):
                if bucket[i] + nums[index] > target: continue
                if i > 0:
                    if bucket[i] == bucket[i-1]: continue
                bucket[i] += nums[index]
                if (backtrack(index + 1, bucket)): return True
                bucket[i] -= nums[index]
            return False

        return (backtrack(0, bucket))
print(Solution().canPartitionKSubsets(nums=[4,3,2,3,5,2,1],k=4))