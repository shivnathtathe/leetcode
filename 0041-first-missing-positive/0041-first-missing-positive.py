class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [x for x in nums if x > 0]

        if not nums:
            return 1

        nums.sort()
        
        if nums[0] != 1:
            return 1

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                return nums[i] + 1

        return nums[-1] + 1
